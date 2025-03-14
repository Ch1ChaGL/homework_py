
# def digital_root(n: int) -> int:
#     value: int = n
#     while n > 9:
#         value = 0
#         while n > 0:
#             value += n % 10
#             n = n // 10
#         n = value
#
#     return value

def digital_root(n: int) -> int:
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

print(digital_root(493193)) #6