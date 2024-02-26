from typing import Any


class Repeater:
    value: Any
    max_count: int
    count: int = 0

    def __init__(self, value: Any, max_count: int) -> None:
        self.value = value
        self.max_count = max_count

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self) -> Any:
        if self.count == self.max_count:
            raise StopIteration
        self.count += 1
        return self.value


repeater = Repeater(5, 7)

for x in repeater:
    print(x, end=' ')

print()

for x in repeater:
    print(x, end=' ')
