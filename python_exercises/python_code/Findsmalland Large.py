from typing import List
def FindSmallAndLarge(arr: List[int]):
    arr.sort()
    return arr

print(FindSmallAndLarge([20,200,34,10]))
print("Small is :", FindSmallAndLarge([20,200,34,10])[0] )
print("Small is :", FindSmallAndLarge([20,200,34,10])[-1] )
