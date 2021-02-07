//Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            return digits[:-1]+[digits[-1]+1]
        i=len(digits)-1
        while digits[i]==9:
            digits[i]=0
            i-=1
        if i<0:
            return [1]+digits
        else:
            return digits[:i]+[digits[i]+1]+digits[i+1:]
