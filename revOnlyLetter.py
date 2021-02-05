//Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        start = 0
        S = list(S)
        end = len(S)-1
        a = range(33, 123, 1)
        while(start<end):
            if not (S[start].isalpha()):
                start+=1
                continue
            if not (S[end].isalpha()):
                end-=1
                continue
            
            S[start], S[end] = S[end], S[start]
            start+=1
            end-=1
            
                
        return "".join(S)
