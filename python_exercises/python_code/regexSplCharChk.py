import re
def regexSplCharChk(s: str, spl: str) -> bool:
    regex = re.compile(spl)

    if(regex.search(s)):
        return True
    else:
        return False
    
print(regexSplCharChk("prakash@gmail", "[@#$]"))
print(regexSplCharChk("prakashgmail", "[@#$]"))


    
        
    