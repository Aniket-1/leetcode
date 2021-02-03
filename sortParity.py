class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        A[::2], A[1::2] = [i for i in A if not 1&i], [i for i in A if 1&i ]
        return A
