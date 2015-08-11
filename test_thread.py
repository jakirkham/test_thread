#!/usr/bin/env python


import ctypes
import sys
import threading
import time


def wait_forever():
    try:
        while True:
            print("Wait for exception...")
            time.sleep(0.1)
    except:
        print(sys.exc_info())


def main(*argv):
    ct = threading.currentThread()

    t = threading.Thread(target=wait_forever)
    t.daemon = True
    t.start()
    t.join(1)

    print(ct.ident)
    print(t.ident)
    print(threading.enumerate())

    print(ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(t.ident), ctypes.py_object(KeyboardInterrupt)))

    t.join(1)

    return(0)


if __name__ == "__main__":
    sys.exit(main(*sys.argv))
