from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n+1)*(n+2)/2
        return int(total - sum(nums))

    
Object = Solution()
print(Object.missingNumber([1, 2, 4, 6, 3, 7, 8]))      



