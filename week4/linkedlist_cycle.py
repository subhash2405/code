# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        dic = set()
        current = head
        while current:
            if current in dic:
                return True
            dic.add(current)
            current = current.next
        return False
# https://leetcode.com/problems/linked-list-cycle/