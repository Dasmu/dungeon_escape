# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 21:23:57 2014

@author: fabio
"""
#==============================================================================
# 
#==============================================================================
class Player(object):
    inventory = []
    
    def __init__(self, name):
        self.name = name
        
    def take_item(self, item):
        self.inventory.put(item)
        
    def show_inventory(self):
        for item in self.inventory:
            print item
    