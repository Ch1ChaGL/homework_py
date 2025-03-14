from typing import List


def sum_two_smallest_numbers(numbers: List[int]) -> int:
    numbers.sort()
    return numbers[0] + numbers[1]


numbers = [19, 5, 42, 2, 77]
print(sum_two_smallest_numbers(numbers))