class Solution:
    def isEqual(self, c1, c2) -> bool:
        if(c1 == '(' and c2 == ')'):
            return True
        if(c1 == '[' and c2 == ']'):
            return True
        if(c1 == '{' and c2 == '}'):
            return True    
        return False
       
    def isValid(self, s: str) -> bool:
        st = []
        for character in s:
            if(len(st) != 0):
                le = st[-1]
                if(self.isEqual(le,character)):
                    st.pop()
                    continue
            st.append(character)
        return len(st) == 0

Object = Solution()
print(Object.isValid('{([])}'))