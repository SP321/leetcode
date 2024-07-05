# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        x=deque(maxlen=3)
        node=head
        ans=[]
        c=0
        mi,mx=inf,-1
        prev,first=None,None
        while node:
            x.append(node.val)
            if len(x)==3 and (x[0]<x[1]>x[2] or x[0]>x[1]<x[2]):
                print(c)
                if first==None:
                    first=c
                else:
                    mx=c-first
                if prev!=None:
                    mi=min(mi,c-prev)
                prev=c
            node=node.next
            c+=1
        if mi==inf:
            return [-1,-1]
        return [mi,mx]
                    