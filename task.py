# -*- coding: utf-8 -*-

def schedule(task):
    while True:
        try:
            task()
            return True
        except Exception, ex: 
            print ex
            import time
            time.sleep(10)



