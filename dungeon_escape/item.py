# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 15:52:54 2014

@author: fabio
"""
from gameobject import GameObject

class Item(GameObject):
    
    def __init__(self, description):
        super(Item, self).__init__(description)
    