from typing  import List
class Solutions:
    def numRescueboatd(self, people: List[int], limit : int) -> int:
        left = 0
        right = len(people)-1
        boats_number = 0
        
        while(left <= right):
            if(left == right):
                boats_number += 1
                break
            
            if(people[left]+people[right] <= limit):
                left += 1
                
            right -= 1
            boats_number += 1
            
        return boats_number
    
    
Object = Solutions()
print(Object.numRescueboatd([1,2,3],3))
    