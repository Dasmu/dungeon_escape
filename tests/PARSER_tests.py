from nose.tools import *
from dungeon_escape.parser import *
from dungeon_escape.lexicon import Lexicon

parser = Parser()
lexicon = Lexicon()

def test_basic():
    result = parser.parse_sentence(lexicon.scan('attack goblin'))
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'attack')
    assert_equal(result.obj, 'goblin')
    
    assert_raises(ParserError, parser.parse_sentence, 'help him')
    assert_raises(ParserError, parser.parse_sentence, 'sword knife eat')
    
    result = parser.parse_sentence(lexicon.scan('knife throw at goblin'))
    assert_equal(result.subject, 'knife')
    assert_equal(result.verb, 'throw')
    assert_equal(result.obj, 'goblin')