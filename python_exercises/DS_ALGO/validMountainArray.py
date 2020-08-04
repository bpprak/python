from typing import List
class Solutions:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A) < 3):
            return False
        
        i = 1 
        while(i < len(A) and A[i] > A[i-1]):
            i += 1
            
        if(i == len(A)):
            return False
        
        while(i < len(A) and A[i] < A[i-1]):
            i +=1
            
        return i == len(A)
    
Object = Solutions()

print(Object.validMountainArray([1,2,4,6,3,2]))
print(Object.validMountainArray([0,5,5]))
print(Object.validMountainArray([2,3,4]))
        
        
#increasing sequence until some point of array and then decrease seqience, like mountain shape
