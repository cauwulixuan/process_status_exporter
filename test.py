#!/usr/bin/python
#-*- coding:utf-8 -*-

import os

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'proc')
print "path:" + path


import os,sys
from subprocess import PIPE,Popen

def process_state(process_name):
    #Linux
    state = 0
    stdout = Popen(['ps aux | grep "' + process_name + '" | grep -v grep'], stdout=PIPE, shell=True)
    output = stdout.stdout.readlines()
    print '||||||process_state||||||process_name|||||| %s' %(process_name)
    print '||||||process_state||||||output|||||| %s' %(output)
    print '||||||length of output : %s||||||' %(len(output))
    # p_checkresp = os.popen('ps aux | grep "' + process_name + '" | grep -v grep').readlines()
    if len(output) >= 1:
        state = 1
    elif len(output) == 0:
        state = 0
    else:
        print "output not correct"
        sys.exit(1)
    return state