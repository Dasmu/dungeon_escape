# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 21:23:57 2014

@author: fabio
"""
#==============================================================================
# Defines a Player
#   player name: defined on game start
#   player bag: container to store found items
#==============================================================================
from item import Item

class Player(object):
    bag = []
    
    def __init__(self, name):
        self.name = name
        self.bag.append(Item('water bottle'))
        
    def take_item(self, item):
        self.bag.append(item)
        
    def show_inventory(self):
        for item in self.bag:
            return item.show_details()
    