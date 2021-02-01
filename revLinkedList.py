//Reverse a Linked List.

#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        rev = None
        while head is not None:
            next_node = head.next
            head.next = rev
            rev = head
            head = next_node
        return rev
