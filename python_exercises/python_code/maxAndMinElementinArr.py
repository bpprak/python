from typing import List
def MaxofArr(arr: List[int])-> int:
    max= arr[0]
    n = len(arr)
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
    return max

def MinofArr(arr: List[int])-> int:
    min= arr[0]
    n = len(arr)
    for i in range(1,n):
        if arr[i]<min:
            min = arr[i]
    return min

print(MaxofArr([30,20,50,40,19]))

print(MinofArr([30,20,50,40,19]))
        