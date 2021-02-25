# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return None
        if head.next == None:
            if head.val == 0:
                return 0
            else:
                return 1
        else:
            l = []
            sum = 0
            while(head):
                l.append(str(head.val))
                head = head.next
            "".join(l)
            for i in range(len(l)-1, -1, -1):
                sum+=(pow(2, i)*int(l[len(l)-1-i]))
            return sum
                
        
