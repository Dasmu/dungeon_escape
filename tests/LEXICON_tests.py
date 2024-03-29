from nose.tools import *
from dungeon_escape.lexicon import Lexicon

lexicon = Lexicon()

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south-west east")
    assert_equal(result, [('direction', 'north'),
                        ('direction', 'south-west'),
                        ('direction', 'east')])
    
def test_actions():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go run attack take throw")
    assert_equal(result, [('verb', 'go'),
                       ('verb', 'run'),
                       ('verb', 'attack'),
                       ('verb', 'take'),
                       ('verb', 'throw')])
    
def test_objects():
    assert_equal(lexicon.scan("knife"), [('noun', 'knife')])
    result = lexicon.scan("knife chest treasure")
    assert_equal(result, [('noun', 'knife'),
                       ('noun', 'chest'),
                       ('noun', 'treasure')])
    
def test_numbers():
    assert_equal(lexicon.scan('1234124'), [('number', 1234124)])
    result = lexicon.scan('12 * 5 = 60')
    assert_equal(result, [('number', 12),
                       ('error', '*'),
                       ('number', 5),
                       ('error', '='),
                       ('number', 60)])
    
def test_errors():
    assert_equal(lexicon.scan("rampadambapenm"), [('error', 'rampadambapenm')])
    result = lexicon.scan("chest football bear sword asdf")
    assert_equal(result, [('noun', 'chest'),
                       ('error', 'football'),
                       ('error', 'bear'),
                       ('noun', 'sword'),
                       ('error', 'asdf')])
    
def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan('in at on of')
    assert_equal(result, [('stop', 'in'),
                       ('stop', 'at'),
                       ('stop', 'on'),
                       ('stop', 'of')])
    
def test_all():
    result = lexicon.scan('go north to kill 1 goblin up there with my sword')
    assert_equal(result, [('verb', 'go'),
                       ('direction', 'north'),
                       ('stop', 'to'),
                       ('verb', 'kill'),
                       ('number', 1),
                       ('noun', 'goblin'),
                       ('direction', 'up'),
                       ('error', 'there'),
                       ('stop', 'with'),
                       ('error', 'my'),
                       ('noun', 'sword')])