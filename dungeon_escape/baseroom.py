#==============================================================================
# BASE CLASE FOR ROOMS
# overwrite enter_unvisited() and enter_visited() to design your rooms 
#==============================================================================

from player import Player

class BaseRoom(object):
    player = None  
    
    def __init__(self, name, description):
        # the name of the room
        self.name = name
        # the description of what is in the room
        self.description = description
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
        
    # **************** BUILD ACTION FOR ROOM ****************
    def enter_unvisited(self):
        # do stuff in the room
        # get at least user input on where to go next
        # before returning the direction
        # set self.visited = True
        return 'north'
    
    def enter_visited(self):
        # maybe do other stuff now
        return 'north'
    
#==============================================================================
#     ROOM LAYOUT FUNCTIONS
#     used to build the room: layout, objects, etc.
#==============================================================================
    
    # updates the room layout
    # @param: Dictionary entry to match directions to rooms: 'direction': room_object
    def add_paths(self, path):
        self.roomLayout.update(path)
    
#==============================================================================
#     GAME ENGINE FUNCTIONS
#     these functions get called by the game engine DO NOT CHANGE!!!
#==============================================================================
    
    # returns the direction to go to
    def enter(self, player):
        self.player = player
        if self.visited == False:
            # enter the room for the first time
            return self.enter_unvisited()
        else:
            # enter the room again
            return self.enter_visited()
        
    # according to direction returns the next room
    def go(self, direction):
        return self.roomLayout.get(direction)