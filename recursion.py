from typing import List, Tuple, Dict, Union, Optional

Number = Union[int, float]


def factorial(x: int) -> int:
    if x <= 1:
        return 1
    return x * factorial(x-1)


def s(a: Number, b: Number, *args, **kwargs) -> Number:
    print(args)
    print(kwargs)
    return a + b + sum(args) + sum(kwargs.values())


# heading как позиционный, а length как именованный
def format_heading(heading, /, separator, *, length: Optional[int]):
    return f'{separator * length} {heading} {separator * length}'


print(format_heading('Hello World', '-', length=5))
print(format_heading('Hello World', separator='*', length=5))

res: int = factorial(5)
print(res)

a: int = 5

print(s(7, 9))
print(s(4, 8, 10, 0, 8, 14))

nums: List[int] = [7, 8, 10, 55]
print(*nums)  # print(7, 8, 10, 55)

info: Tuple[str, str, int] = ('Ivanov', 'Ivan', 27)

print(s(a=10, b=20, c=30))
print(s(22.7, 69, 77.19))

data: Dict[str, int] = {
    'a': 5,
    'b': 9,
    'c': 13,
    'd': 4
}

# data['sdfsdf'] = 'sdfsdf'
# data[98] = 88

print(s(a=10, b=20, c=30))
print(s(**data))
