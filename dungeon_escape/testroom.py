# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 23:16:54 2014

@author: fabio
"""
from baseroom import BaseRoom

class TestRoom(BaseRoom):
    def enter_unvisited(self):
        print 'You are in %s' % self.name
        print self.description
        return raw_input('> ')
        
    def enter_visited(self):
        return self.enter_unvisited()