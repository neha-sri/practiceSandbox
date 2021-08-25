# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        merged = ListNode()
        merged_head = merged

        while p1 and p2:
            if p1.val < p2.val:
                merged.next = ListNode(p1.val)
                p1 = p1.next
            else:
                merged.next = ListNode(p2.val)
                p2 = p2.next
            
            merged = merged.next

        while p1:
            merged.next = ListNode(p1.val)
            p1 = p1.next
            merged = merged.next

        while p2:
            merged.next = ListNode(p2.val)
            p2 = p2.next
            merged = merged.next 

        return merged_head.next
