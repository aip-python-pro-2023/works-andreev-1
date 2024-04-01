from random import randint


def repeater(v):
    while True:
        print('Hello!')
        yield v


def random_numbers():
    while True:
        yield randint(0, 1000000)


def fibonacci():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b


for i, value in enumerate(fibonacci()):
    print(i, value)
    if i == 50:
        break
