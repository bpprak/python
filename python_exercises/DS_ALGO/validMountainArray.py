from typing import List
class Solutions:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A) < 3):
            return False
        
        i = 1 
        while(i < len(A) and A[i] > A[i-1]):
            i += 1
            
        if(i ==1 or i == len(A)):
            return False
        
        while(i < len(A) and A[i] < A[i-1]):
            i +=1
            
        return i == len(A)
    
Object = Solutions()

print(Object.validMountainArray([1,2,4,6,3,2]))
        