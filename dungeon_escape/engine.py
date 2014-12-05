from map import Map
from player import Player
from room import Room

class Engine(object):
	room_history = []
	
	def __init__(self, player, start_room):
         self.new_player = player
         self.start_room = start_room
            
		
	def play(self):
		current_room = self.start_room
		
		while True:
			print "-" * 10
			direction_name = current_room.enter()
			self.room_history.put(current_room)
			current_room = current_room.go(direction_name)
