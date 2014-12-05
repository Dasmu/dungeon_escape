# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 21:23:57 2014

@author: fabio
"""
#==============================================================================
# 
#==============================================================================
from item import Item

class Player(object):
    inventory = []
    
    def __init__(self, name):
        self.name = name
        self.inventory.append(Item('water bottle'))
        
    def take_item(self, item):
        self.inventory.append(item)
        
    def show_inventory(self):
        for item in self.inventory:
            return item.show_details()
    