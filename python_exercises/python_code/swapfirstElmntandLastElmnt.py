from typing import List
def swapList(arr: List[int]):
    temp = arr[0]
    arr[0]= arr[-1]
    arr[-1]= temp
    
    return arr

print(swapList([1,3,83,89]))

def swapListwithoutvar(arr: List[int]):
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr


print(swapListwithoutvar([1,3,83,89]))
    