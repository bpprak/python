def Factorial(num: int )-> int:
    if(num ==0 or num <0):
        return 1
    else:
        return num*Factorial(num-1)
    
print(Factorial(5))