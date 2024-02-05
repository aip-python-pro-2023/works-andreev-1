def log(func):
    def wrapper(*args, **kwargs):
        print('Function is called')
        return func(*args, **kwargs)
    return wrapper


@log
def get_multiplier(x):
    def multiply(a):
        return a * x

    return multiply


@log
def greet():
    print("Hello")


greet()

triple = get_multiplier(3)
print(triple(5))
