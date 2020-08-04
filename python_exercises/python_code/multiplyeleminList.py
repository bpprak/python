from typing import List
def multiplyele(arr: List[int]) -> int:
    m = 1
    for i in range(0,len(arr)):
        m = m * arr[i]
    return m

print(multiplyele([3,2,4]))

