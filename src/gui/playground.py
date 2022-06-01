def add(*args):
    summa = 0
    for n in args:
        summa += n
    return summa


# print(add(1, 2, 5, 6, 4, 3, 2, 4, 6, 7, 0))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')


my_car = Car(make='Nissan', model='GT-R')

print(my_car.model)
