from typing import List
class Solution:
    def moveZeroesfirst(self, nums: List[int]) -> None:
        j = 0
        for num in nums:
            if(num != 0):
                nums[j] = num
                j += 1
                
        
        for x in range(j, len(nums)):
            nums[x] = 0
    

        return(nums[::-1])


Object = Solution()
x = [1,0,4,0,5,9,3,9,0,2,0]
print(Object.moveZeroesfirst(x))
