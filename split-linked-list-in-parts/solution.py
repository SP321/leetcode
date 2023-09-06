# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
            
        partlength, extra = divmod(n, k)
        
        ans = []
        cur = head
        for i in range(k):
            dummy = ListNode(0)
            write = dummy
            
            for j in range(partlength + (i < extra)):
                write.next = ListNode(cur.val)
                write = write.next
                if cur:
                    cur = cur.next
            
            ans.append(dummy.next)
        return ans