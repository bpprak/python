class Solution:
    def Factorial(self, num: int) -> str:
        factorial =1
        
        if(num<0):
            print("No Factorial for negative No's")
        elif(num == 0):
            print("The factorial for 0 is 1")
        else:
            for i in range(1, num+1):
                factorial= factorial*i
            return factorial
    
            
Object = Solution()
print("The Factorial is", Object.Factorial(5))

