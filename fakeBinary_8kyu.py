

def fake_bin(str: str) -> str:
    return ''.join(['0' if int(x) < 5 else '1' for x in str])


numbers = '45385593107843568'

print(fake_bin(numbers))