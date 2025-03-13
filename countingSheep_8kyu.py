from typing import List


def count_sheeps(sheep: List[bool]) -> int:
    return sum(x for x in sheep if x == True)

a = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
print(count_sheeps(a))
