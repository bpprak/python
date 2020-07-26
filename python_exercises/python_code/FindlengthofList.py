from typing import List
def FindLen(arr: List[int])-> int:
    count = 0
     
    for i in arr:
        count+= 1
        
    return count

print(FindLen([1,2,3,4,5,6]))