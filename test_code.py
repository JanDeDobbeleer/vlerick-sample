from code import get_max_number, get_a_chuck_norris_joke
from jokyjokes import chucknorris

def test_get_max_number_1_larger_than_0():
    highest = get_max_number(0,1)
    assert highest == 1

def test_get_max_number_10_larger_than_2():
    highest = get_max_number(10,2)
    assert highest == 10

def test_get_max_number_no_numbers():
    highest = get_max_number('test','crazy')
    assert highest == 'test'

def test_get_a_chuck_norris_joke():
    joke = get_a_chuck_norris_joke()
    assert joke in chucknorris.all_jokes()
