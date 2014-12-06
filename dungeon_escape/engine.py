from player import Player
from baseroom import BaseRoom

class Engine(object):
	room_history = []
	
	def __init__(self, new_player, start_room):
         self.player = new_player
         self.start_room = start_room
            
		
	def play(self):
		current_room = self.start_room
		
		while True:
			print "-" * 10
			direction_name = current_room.enter(self.player)
			self.room_history.append(current_room)
			current_room = current_room.go(direction_name)
