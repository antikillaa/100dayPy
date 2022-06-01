def add(*args):
    summa = 0
    for n in args:
        summa += n
    return summa


print(add(1, 2, 5, 6, 4, 3, 2, 4, 6, 7, 0))
