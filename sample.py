def f(x, a=None):
    if a is None:
        a = []
    a.append(x)
    print(id(a))
    print('Appended element to list')
    return a


data = f(5)
print(id(data))
data = f(9)
print(id(data))
data = f(11)
print(id(data))
print(data)
