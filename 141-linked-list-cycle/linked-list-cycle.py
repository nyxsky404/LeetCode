# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()
        curr = head
        while curr is not None:
            if curr not in my_set:
                my_set.add(curr)
                curr = curr.next
            else:
                return True
        return False
                    