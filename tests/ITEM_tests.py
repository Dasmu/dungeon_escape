from nose.tools import *
from dungeon_escape.item import Item

def test_basic():
    text = "This is an item"
    item = Item(text)
    assert_equal(item.description, text)
    assert_equal(item.show_details(), text)