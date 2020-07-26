import math
class Solutions:
    def countprimes(self, n: int) -> int:
        if n<2:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2, math.ceil(math.sqrt(n))):
            if isPrime[i]:
                for multiples_of_i in range(i*i, n, i):
                    isPrime[multiples_of_i] = False
                    
                
        return sum(isPrime)
        
Object = Solutions()
print(Object.countprimes(34))