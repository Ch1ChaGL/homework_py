from functools import reduce
from typing import List


a = [1, 2, 2]


def square_sum(numbers: List[int]) -> int:
    return reduce(lambda acc, num: acc + num**2, numbers, 0)


def square_sum2(numbers: List[int]) -> int:
    return sum(x**2 for x in numbers)

print(square_sum(a))