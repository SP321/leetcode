# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1e5)
        current = dummy

        while any(lists):
            min_index = -1
            min_val = float('inf')
            for i, l in enumerate(lists):
                if l and l.val < min_val:
                    min_val = l.val
                    min_index = i

            if min_index != -1:
                current.next = lists[min_index]
                current = current.next
                lists[min_index] = lists[min_index].next

        return dummy.next