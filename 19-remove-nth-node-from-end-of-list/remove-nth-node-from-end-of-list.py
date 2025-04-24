# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        temp = head
        while temp is not None:
            len +=1
            temp = temp.next


        prev = None
        curr = head

        # if empty
        if curr is None:
            return None

        # first element
        elif n == len:
            curr = head
            if curr.next is not None:
                head = curr.next
            else:
                head = None

        # nth and last element

        elif curr is not None:
            x = len - n + 1
            
            for i in range(1,x):
                prev = curr
                curr = curr.next
            
            if curr.next is not None:
                prev.next = curr.next
            else:
                prev.next = None
        
        return head