from typing import List
def listcopy(myList: List[int]) -> List[int]:
    newlist =[i for i in myList]
    return newlist

print(listcopy([4,8,2,3,0]))