#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import sys
import re
import time
import argparse
import logging
import psutil

from subprocess import Popen, PIPE
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')
import sys
logger = logging.getLogger(sys.path[0] + 'process_status_exporter')

class ProcessStatusCollector(object):
    """collect process status"""
    def __init__(self):
        pass

    def collect(self):
        # The metrics we want to export.
        process_info = get_process_name()
        for process_name in process_info:
            print 'process_name = %s ' % (process_name)
            pid = get_pid(process_name)
            print 'PID = %s ' % (pid)
            snake_case = re.sub('[-|\s]', r'_', process_name).lower()

            yield GaugeMetricFamily(snake_case + '_process_up',
                                    snake_case + ' Process Up or Down (1 for up, 0 for down).',
                                    value = process_state(pid))

            process_metrics = get_process_metrics(pid, process_name)
            if process_metrics:
                yield GaugeMetricFamily(snake_case + '_running_time_seconds_total',
                                        snake_case + ' Total Running time in seconds.',
                                        value = process_metrics['create_time'])
                yield GaugeMetricFamily(snake_case + '_cpu_percentage',
                                        snake_case + ' CPU Percentage.',
                                        value = process_metrics['cpu_percent'])
                yield GaugeMetricFamily(snake_case + '_opened_fds_number',
                                        snake_case + ' Total Number of Opened fds.',
                                        value = process_metrics['num_fds'])
                yield GaugeMetricFamily(snake_case + '_threads_number',
                                        snake_case + ' Total Number of Threads.',
                                        value = process_metrics['num_threads'])
                yield GaugeMetricFamily(snake_case + '_opened_files_number',
                                        snake_case + ' Total Number of opened files.',
                                        value = process_metrics['open_files'])
                
                # OrderedDict([('read_count', 49566766), ('write_count', 29218473), ('read_bytes', 269357056), ('write_bytes', 4311138304), ('read_chars', 3803556911), ('write_chars', 7421457950)])
                io_counter = GaugeMetricFamily(snake_case + '_io_counters',
                                               snake_case + ' IO counters.',
                                               labels = ['type'])
                
                for key in process_metrics['io_counters'].keys():
                    io_counter.add_metric([key], process_metrics['io_counters'][key])
                yield io_counter

                # pcputimes(user=10388.04, system=5887.69, children_user=0.0, children_system=0.0)
                cpu_times = GaugeMetricFamily(snake_case + '_cpu_time_seconds_total',
                                              snake_case + ' Total CPU time in seconds.',
                                              labels = ['mode'])
                for key in process_metrics['cpu_times'].keys():
                    cpu_times.add_metric([key], process_metrics['cpu_times'][key])
                yield cpu_times                

                # pfullmem(rss=29552640, vms=84586496, shared=12046336, text=11493376, lib=0, data=25661440, dirty=0, uss=30842880, pss=30842880, swap=0)
                memory_info = GaugeMetricFamily(snake_case + '_memory_usage_bytes_total',
                                               snake_case + ' Memory Usage by each mode.',
                                               labels = ['mode'])
                for key in process_metrics['memory_info'].keys():
                    memory_info.add_metric([key], process_metrics['memory_info'][key])
                yield memory_info

            else:
                pass

def get_process_name():
    # select process_name from process_info.txt
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'process_info.txt')) as file:
            for process_name in file:
                if process_name.startswith('#') or process_name.strip() == '':
                    continue
                else:
                    yield process_name.rstrip()
    except IOError:
        logging.error("open files error, please check!")
        pass


def get_pid(process_name):
    '''
    This function is able to get PID by a given process name. Usually PID can be found in a .pid file 
    located in /run/ directory, or in /run/service_dir/ directory. If no pid file exist in the directories
    mentioned above, and if the program was setup by systemctl, PID can still be found in a cgroup.procs 
    file, which usually located in /sys/fs/cgroup/systemd/system.slice/process_name.service/ directory.

    @process_name: read process_name from process_info.txt file. 
    @return: return a PID(string type) of the given process_name.
    '''
    if os.path.exists(r'/run/{0}/{0}.pid'.format(process_name)):
        logging.info("/run/{0}/{0}.pid file exist, read PID.".format(process_name))
        with open("/run/{0}/{0}.pid".format(process_name), "r") as f:
            data = f.readline().rstrip()
            return data
    elif os.path.exists(r'/run/{0}.pid'.format(process_name)):
        logging.info("/run/{0}/{0}.pid file not exist, /run/{0}.pid file exist, read PID.".format(process_name))
        with open("/run/{0}.pid".format(process_name), "r") as f:
            data = f.readline().rstrip()
            return data
    elif os.path.exists(r'/sys/fs/cgroup/systemd/system.slice/{0}.service/cgroup.procs'.format(process_name)):
        logging.info("no pid file in /run/ directory. .../{0}.service/cgroup.procs file exist, read PID.".format(process_name))
        with open("/sys/fs/cgroup/systemd/system.slice/{0}.service/cgroup.procs".format(process_name), "r") as f:
            data = f.readline().rstrip()
            return data
    elif "knox-server" in process_name:
        logging.info("/run/knox/gateway.pid file exist, read PID.")
        with open("/run/knox/gateway.pid", "r") as f:
            data = f.readline().rstrip()
            return data
    else:
        logging.error("Cann't find {0} PID file, error happened, please check why PID file not exist.".format(process_name))
        sys.exit(1)

def get_process_metrics(pid, process_name):
    '''
    This function is setup to scrape process metrics, such as CPU, Mem, uptime, status and so on.
    All the metrics can be scraped in the /proc/pid/stat file. However, here I uesed a third-party liberary "psutil" 
    to get all data I need.
    @pid: PID get by get_pid() function.
    @return: return a list of all metrics I need.
    '''
    process_metrics = {}
    try:
        process = psutil.Process(int(pid))
        process_metrics = {
            "create_time" : process.create_time(),
            "io_counters" : process.io_counters()._asdict(),
            "cpu_times" : process.cpu_times()._asdict(),
            "cpu_percent" : process.cpu_percent(),
            "memory_info" : process.memory_full_info()._asdict(),
            "num_fds" : process.num_fds(),
            "num_threads" : process.num_threads(),
            "open_files" : len(process.open_files())
        }
    except:
        logging.error("No pid {0} found, please check ! ".format(process_name))
        pass
    return process_metrics


def process_state(pid):
    # Linux
    state = 0
    output = Popen(['ps aux | grep -i "' + pid + '" | grep -v grep'],
                    stdout=PIPE,
                    shell=True)
    # close_fds=True)
    result = output.stdout.readlines()
    if len(result) >= 1:
        state = 1
    elif len(result) == 0:
        logging.error('process {0} down, please check!'.format(pid))
        state = 0
    else:
        pass
    print 'state = %s' % (state)
    return float(state)


def _parse_stat_file(pid):
    """Parse /proc/{pid}/stat file. Return a list of fields where
    process name is in position 0.
    Using "man proc" as a reference: where "man proc" refers to
    position N, always substract 2 (e.g starttime pos 22 in
    'man proc' == pos 20 in the list returned here).
    The return value is cached in case oneshot() ctx manager is
    in use.
    """
    with open("/proc/{0}/stat".format(pid), "rb") as f:
        data = f.read()
    # Process name is between parentheses. It can contain spaces and
    # other parentheses. This is taken into account by looking for
    # the first occurrence of "(" and the last occurence of ")".
    rpar = data.rfind(b')')
    name = data[data.find(b'(') + 1:rpar]
    others = data[rpar + 2:].split()
    return [name] + others

def parse_args():
    parser = argparse.ArgumentParser(
        description='process status exporter args, including address and port'
    )
    parser.add_argument(
        '--telemetry-path',
        metavar='telemetry_path',
        required=False,
        help='Path under which to expose metrics. (default "/metrics")',
        default='/metrics'
    )
    parser.add_argument(
        '--address',
        metavar='address',
        required=False,
        help='Running on this address. (default "127.0.0.1")',
        default='127.0.0.1'

    )
    parser.add_argument(
        '-p', '--port',
        metavar='port',
        required=False,
        type=int,
        help='Listen to this port. (default ":9108")',
        default=int(os.environ.get('VIRTUAL_PORT', '9108'))
    )
    return parser.parse_args()


def main():
    try:
        args = parse_args()
        port = int(args.port)
        REGISTRY.register(ProcessStatusCollector())
        start_http_server(port)
        print "Polling %s. Serving at port: %s" % (args.address, port)
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        print "Interrupted"
        sys.exit(0)

if __name__ == "__main__":
    main()
    