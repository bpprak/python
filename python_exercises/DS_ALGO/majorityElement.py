from typing import List
class Solution:
    def majorityElement(self,nums: List[int]) -> int:
        m ={}
        for num in nums:
            m[num] = m.get(num,0)+1
            print(len(nums))
            #print(m)
        for num in nums:
            #print(m[num])
            if(m[num] > len(nums)//2):
                #print(m[num])
                return num
            
object = Solution()
print(object.majorityElement([1,2,3,1]))
            