# -*- coding: utf-8 -*-

import os
import errno


def ensure_path(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def save(filename, content):
    import os
    path = os.path.dirname(filename)
    if path:
        ensure_path(path)

    import io
    f = open(filename, 'w')
    f.write(content)
    f.close()


def read(filename):
    import os
    if os.path.exists(filename):
        f = open(filename, 'r')
        content = f.read()
        f.close()
        return content
    return None


def save_json(filename, obj):
    import simplejson
    content = simplejson.dumps(obj)
    save(filename, content)


def read_json(path):
    import simplejson
    return simplejson.load(open(path))


def read_int(filename, default=0):
    d = read(filename)
    return int(d) if d else default


def save_int(filename, value):
    save(filename, '%d' % value)


def files_in_path(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def schedule(task, wait_time=10):
    try:
        task()
        return True
    except Exception, ex:
        print ex
        import time
        time.sleep(wait_time)
        return False

data_root = 'data'

def data_path(sub_path, filename):
    import os
    path = os.path.join(data_root, sub_path)
    return os.path.join(path, filename)


