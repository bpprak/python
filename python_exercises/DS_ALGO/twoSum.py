from typing import List, DefaultDict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = DefaultDict(int)
        n = len(nums)
        
        for i in range(0,n):
            goal = target - nums[i]
            if(goal in m):
                return (m[goal], i)
            m[nums[i]] = i
            
object = Solution()
print(object.twoSum([3,6,12,14], 15))

            
    