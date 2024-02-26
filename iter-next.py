data = {9, 7, 6, 8, 9}

# Получаем итератор списка (объект, который по нему проходится)
iterator = iter(data)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

while True:
    try:
        x = next(iterator)
    except StopIteration:
        break

    print(x)

# for x in data:
#     print(x)
