from nose.tools import *
from dungeon_escape.player import Player

def test_basics():
    player = Player('Hans')
    assert_equal(player.show_inventory(), 'water bottle')
    assert_equal(player.name, 'Hans')
     
	