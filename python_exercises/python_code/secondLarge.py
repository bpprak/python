from typing import List
def SecondLargest(arr: List[int]):
    arr.sort()
    return arr

print(SecondLargest([20,200,34,10]))
print("Small is :", SecondLargest([20,200,34,10])[-2] )
