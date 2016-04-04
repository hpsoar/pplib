# -*- coding: utf-8 -*-

def schedule(task):
    while True:
        if try_task(task):
            break

def try_task(task):
    try:
        task()
        return True
    except Exception, ex: 
        print ex
        import time
        time.sleep(10)
        return False




