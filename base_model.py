# -*- coding: utf-8 -*-
import ff
import copy

class BaseM(object):
    def __str__(self):
        return unicode(self).encode('utf-8')


    def __unicode__(self):
        return ff.format_object(self.dump_object())


    def dump_object(self):
        return copy.deepcopy(self.__dict__)

