# -*- coding: utf-8 -*-

import os
import errno
from bs4 import BeautifulSoup as Soup

def BSFile(filename):
    return Soup(open(filename))

def BS(conent):
    return Soup(content)

def url_to_filename(url):
    import base64
    return base64.urlsafe_b64encode(url)


def openfile(path, mode):
    dir_name = os.path.dirname(path)
    if dir_name:
        ensure_path(dir_name)

    return open(path, mode)


def ensure_path(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def exists(path):
    return os.path.exists(path)

def filenames_inpath(path):
    from os import listdir
    from os.path import isfile, join
    return [join(path, f) for f in listdir(path) if isfile(join(path, f))]


def save(filename, content, mode='w'):
    import os
    path = os.path.dirname(filename)
    if path:
        ensure_path(path)

    f = open(filename, mode)
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
    if os.path.exists(path):
        return simplejson.load(open(path))
    else:
        return None


def read_lines(path):
    c = read(path)
    return c.split('\n') if c else list()


def read_int(filename, default=0):
    d = read(filename)
    return int(d) if d else default


def read_states(filename, default=None):
    d = read(filename)
    return d.split(',') if d else default


def save_states(filename, states):
    state_str = ','.join(states)
    save(filename, state_str)


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


def format_object(o):
    import json
    return json.dumps(o, ensure_ascii=False, indent=4)


def enum_lines(f, callback, strip=True):
    for l in open(f):
        if strip:
            l = l.strip()
        callback(l)


def enum_lines2(f, callback, strip=True, sep='\t'):
    def _callback(l):
        parts = l.split(sep)
        if strip:
            parts = [p.strip() for p in parts]
        callback(l, parts)

    enum_lines(f, _callback, False)

