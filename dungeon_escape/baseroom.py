#==============================================================================
# BASE CLASE FOR ROOMS
# overwrite enter_unvisited() and enter_visited() to design your rooms 
#==============================================================================

from player import Player
from gameobject import GameObject

class BaseRoom(object):
    player = None
    inventory = []
    
    def __init__(self, name, description):
        # the name of the room
        self.name = name
        # the description of the room (including exits and objects)
        self.description = description
        self.directions = description
        self.objects = description
        self.visited = False
        # the basic room Layout 10-directional
        # every room is an octagon and can have a room above or below
        self.roomLayout = {'north': None,
                'north-east': None,
                'east': None,
                'south-east': None,
                'south': None,
                'south-west': None,
                'west': None,
                'north-west': None,
                'up': None,
                'down': None}
#==============================================================================
#   BUILD ACTION FOR ROOM
#==============================================================================
    def enter_unvisited(self):
        # do stuff in the room
        # get at least user input on where to go next
        return 'north'
    
    def enter_visited(self):
        # maybe do other stuff now
        # or just return self.enter_unvisited() 
        return 'north'
    
#==============================================================================
#     ROOM LAYOUT FUNCTIONS
#     used to build the room: layout, objects, etc.
#==============================================================================
    
    # updates the room layout
    # @param: Dictionary entry to match: 'direction': room_object
    def add_paths(self, path):
        self.roomLayout.update(path)
        
    # optional: describe where to find exits separately
    def describe_layout(self, description):
        self.directions = description
    
    # optional: describe what objects to find in the room   
    def describe_objects(self, description):
        self.objects = description
    
    # adds a new GameObject to the room's inventory
    def add_objects(self, new_object):
        self.inventory.append(new_object)
    
#==============================================================================
#     GAME ENGINE FUNCTIONS
#     these functions get called by the game engine DO NOT CHANGE!!!
#==============================================================================
    
    # puts the player into the room,
    # calls the self defined room functions
    # returns the direction the player wants to take to the game engine
    def enter(self, player):
        self.player = player
        if self.visited == False:
            # enter the room for the first time
            next_room = self.enter_unvisited()
            self.visited = True
            return next_room
        else:
            # enter the room again
            next_room = self.enter_visited()
            return next_room
        
    # according to direction returns the next room
    def go(self, direction):
        return self.roomLayout.get(direction)