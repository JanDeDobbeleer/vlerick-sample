from jokyjokes import chucknorris

def get_max_number(a,b):
    if a > b:
        return a
    return b

def get_a_chuck_norris_joke():
    return chucknorris.random()
