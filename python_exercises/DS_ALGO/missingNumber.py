from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        currentSum = sum(nums)
        n = len(nums)
        intendedSum = (n)*(n+1)/2

        return int(intendedSum-currentSum)

    
Object = Solution()
print(Object.missingNumber([4,1,2]))      