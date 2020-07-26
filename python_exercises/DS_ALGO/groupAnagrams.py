from    typing import List
class Solution:
    def hashed(self, s):
        return ''.join(sorted(s))
    
    def groupAnagrams(self, strs: List[int]) -> List[List[int]]:
        m = {}
        answers = []
        
        for s in strs:
            hashed = self.hashed(s)
            if(hashed not in m):
                m[hashed] = []
            m[hashed].append(s)
            
        for v in m.values():
            answers.append(v)
            
        return answers
    
Object = Solution()
print(Object.groupAnagrams(['prak','krap', 'beno','onbe','fel', 'lef', 'ler']))
            
                
            
        