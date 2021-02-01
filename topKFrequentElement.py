//Given a non-empty array of integers, return the k most frequent elements.

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        l = []
        d = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
        n = 0
        for key, v in d.items():
            if n == k:
                break
            l.append(key)
            n+=1
        return l
            
