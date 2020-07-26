def Primecheck(num: int) -> str:
    count =0
    
    if num>1:
        for i in range(1,num+1):
            if(num%i == 0):
                count += 1
        
        if(count == 2):
            print("Number s prime")
        else:
            print("Number is not prime")
        
Primecheck(10)
Primecheck(3)
