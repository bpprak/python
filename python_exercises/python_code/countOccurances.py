from typing import List
def countOccurances(arr: List[int], o: int) -> int:
    count= 0
    for i in range(0,len(arr)):
        if(arr[i] == o):
            count += 1
    return count

print(countOccurances([12,3,5,6,10,23,53,67,10], 10))

def countOccurances2(arr: List[int], o: int) -> int:
    count= 0
    for i in arr:
        if(i == o):
            count += 1
    return count

print(countOccurances2([12,3,5,6,10,23,53,67,10], 10))