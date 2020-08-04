from typing import List
def SumofList(mylist: List[int]) -> int:
    total = 0
    for i in mylist:
        total=total+i
    return total

print(SumofList([1,2,3,4,5]))