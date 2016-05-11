# -*- coding: utf-8 -*-
import ff
import copy


class BaseM(object):
    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return ff.format_object(self.dump_object())

    def dump_object(self):
        props = self.properties_to_dump()
        o = dict()
        for k in props:
            o[k] = BaseM.transform_prop(k, self.dict__property(k))
        return copy.deepcopy(o)

    def dict__property(self, k):
        return self.__dict__[k]

    def property_map(self):
        return self.__dict__

    def properties_to_dump(self):
        return self.__dict__.keys()

    @staticmethod
    def transform_prop(key, value):
        return value


class ClassPropertyDescriptor(object):

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def setter(self, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self    


def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)

    return ClassPropertyDescriptor(func)

