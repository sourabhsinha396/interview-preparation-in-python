class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        bijection_map = {}
        s = s.split()
        
        if len(pattern)!=len(s):
            return False
        
        for index,char in enumerate(pattern):
            if bijection_map.get(char) is None:
                bijection_map[char] = s[index]
            elif bijection_map.get(char)!=s[index]:
                print(bijection_map.get(char),s[index])
                return False
            
        reverse_map = {}
        for index,word in enumerate(s):
            if reverse_map.get(word) is None:
                reverse_map[word] = pattern[index]
            elif reverse_map.get(word) != pattern[index]:
                return False
        return True