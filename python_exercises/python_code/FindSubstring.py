def FindSubstring(s1: str, s2: str) -> bool:
    wordlist = s1.split(" ")
    count =0
    for i in range(0, len(wordlist)):
        if(wordlist[i] == s2):
            count += 1
    if(count > 0):
        return True
    else:
         return False
            
    

        
        

print(FindSubstring("Hi hello im im", "im"))
print(FindSubstring("Hi hello im im", "imq"))
    
    
    
    
    