# -*- coding: utf-8 -*-
__author__ = 'huangpeng'


class AGList(list):
    def each(self, func):
        for a in self:
            func(a)
        return self

    def map(self, func):
        return map(func, self)

    def filter(self, func):
        return filter(func, self)


class AGDict(dict):
    def each(self, func):
        for (k, v) in self.items():
            func(k, v)
        return self

    def map(self, func):
        return map(func, self)

    def filter(self, func):
        return filter(func, self)
