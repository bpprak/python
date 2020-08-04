from typing import List
def removeNthEl(mylist: List[int], word: str, n : int) -> List[int]:
    count = 0
    for i in range(0, len(mylist)):
        if(mylist[i] == word):
            count +=1
            if(count == n):
                del mylist[i]
    return mylist

print(removeNthEl(["Hi", "how" , "are", "Hi"], "Hi", 2))

        