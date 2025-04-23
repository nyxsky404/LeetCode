# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head
        else:
            prev = None
            curr = head

            while curr is not None :
                front = curr.next
                curr.next = prev
                prev = curr
                curr = front
                

            return prev

        