import commands, os, re

def process_info(pid):
    res = commands.getstatusoutput('ps aux|grep '+str(pid))[1].split('\n')[0]
    compile = re.compile(r'\s+')  
    result = compile.split(res)  
    info = {'user':result[0],  
        'pid':result[1],  
        'cpu':result[2],  
        'mem':result[3],  
        'vsa':result[4],  
        'rss':result[5],  
        'start_time':result[6]}  
    return info

import psutil
from time import time
def start_time(pid):
	proc = psutil.Process(pid)
	start_time = proc.create_time()
	time_inter = time() - start_time
	return time_inter
