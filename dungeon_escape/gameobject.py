# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 15:49:58 2014

@author: fabio
"""

class GameObject(object):
        description = "no description available"
        def __init__(self, description):
            self.description = description
            
        def show_details(self):
            return self.description