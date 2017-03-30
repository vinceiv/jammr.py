#!/usr/bin/pythonw

import thread



def printThread(num):
    print("thread num: ", num)

if __name__ == '__main__':
    for x in range(0,100):
        thread.start_new_thread(printThread(x))
