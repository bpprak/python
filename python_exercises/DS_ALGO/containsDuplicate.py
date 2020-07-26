from typing import List
class Solution:
    def containDuplicate(self, nums: List[int]) -> bool:
        m = {}
        
        for num in nums:
            if(num in m):
                return True
            m[num] = 1
        return False
    
object = Solution()
print(object.containDuplicate([1,2,3,5,5]))
            