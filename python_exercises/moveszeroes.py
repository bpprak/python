from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for num in nums:
            print(nums)
            if(num != 0):
                nums[j] = num
                j += 1
                
        
        for x in range(j, len(nums)):
            nums[x] = 0
    

        return(nums)


Object = Solution()
x = [1,0,4,0,5]
print(Object.moveZeroes(x))
