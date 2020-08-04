from typing import List
def swapantTwo(arr: List[int], pos1: int, pos2: int) -> List[int]:
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

print(swapantTwo([1,2,4,7,8,20],0, 4))


    