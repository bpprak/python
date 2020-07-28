def palindrome(s: str)-> bool:
    rev = s[::-1]
    if(rev == s):
        return True
    else:
        return False
    
print(palindrome("madam"))
print(palindrome("abcedf"))