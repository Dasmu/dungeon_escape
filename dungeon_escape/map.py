from testroom import TestRoom
from engine import Engine

startroom = TestRoom('a prison cell', 'door to the west')
first = TestRoom('the guard room', 'door to the north and to the east')
second = TestRoom('an ante Room', 'door to the east and to the south')
third = TestRoom('a small chamber', 'door to the south-east and to the west')
fourth = TestRoom('a big hall', 'door to the south-west and to the north-west')
fifth = TestRoom('a cellar', 'door to the south-east and to the north-east')
sixth = TestRoom('a long corridor', 'door to the north-east and to the north-west')
seventh = TestRoom('a bedroom', 'door to the north-east and to the south-west')
eighth = TestRoom('a bathroom', 'window to the north-east and to the south-west')

startroom.add_paths({'west': first})
first.add_paths({'east': startroom, 'north': second})
second.add_paths({'south': first, 'east': third})
third.add_paths({'west': second, 'south-east': fourth})
fourth.add_paths({'north-west': third, 'south-west': fifth})
fifth.add_paths({'north-east': fourth, 'south-east': sixth})
sixth.add_paths({'north-west': fifth, 'north-east': seventh})
seventh.add_paths({'south-west': sixth, 'north-east': eighth})
eighth.add_paths({'south-west': seventh})

game_engine = Engine('TestPlayer', startroom) 
print 'Welcome to Dungeon Escape %s' % game_engine.player
game_engine.play()