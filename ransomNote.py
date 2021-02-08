//Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

//Each letter in the magazine string can only be used once in your ransom note.

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote=="":
            return True
        rn = Counter(ransomNote)
        mg = Counter(magazine)
        flag = 1
        for k,v in rn.items():
            if mg[k]>=v:
                flag = 0
            else:
                flag = 1
                break
                
        if flag == 1:
            return False
        return True
        
