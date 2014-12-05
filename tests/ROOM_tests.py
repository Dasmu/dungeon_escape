from nose.tools import *
from dungeon_escape.room import Room

def test_room():
	gold = Room("GoldRoom", 
			 """This room has gold in it you can grab. There's a
			 door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.roomLayout, {'north': None,
				'north-east': None,
				'east': None,
				'south-east': None,
				'south': None,
				'south-west': None,
				'west': None,
				'north-west': None,
				'up': None,
				'down': None})
	
def test_room_paths():
	center = Room("Center", "Test the room in the center.")
	north = Room("North", "Test the room in the north.")
	south = Room("South", "Test the room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)
	
def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'), west)
	assert_equal(start.go('down'), down)
	assert_equal(west.go('east'), start)
	assert_equal(down.go('up'), start)
	
#==============================================================================
# def test_enter():
# 	start = Room("Start", "You can go up.")
# 	attic = Room("Attic", "You can go down.")
# 	start.enter()
# 	attic.enter()
# 	assert_equal(start.visited, True)
# 	assert_equal(attic.visited, True)
#==============================================================================
	