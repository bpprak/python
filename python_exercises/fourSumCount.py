from typing import List
class Solution:
    def fourSumcount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        m ={}
        
        for i in range(0, len(A)):
            x = A[i]
            for j in range(0, len(B)):
                y = B[j]
                if(x+y not in m):
                    m[x+y] = 0
                m[x+y] += 1
                print(m)
                
        for i in range(0, len(C)):
            x = C[i]
            for j in range(0,  len(D)):
                y = D[j]
                target = -(x+y)
                if(target in m):
                    ans += m[target]
                    print(ans)
            #print(m)
        return ans
 
                 
Object = Solution()
print(Object.fourSumcount([1,2],[-2,-1],[-1,2],[1,2]))      
  
                    
        
