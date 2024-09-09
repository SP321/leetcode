# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1] * n for _ in range(m)]

        x1, y1 = 0,0
        x2, y2 = m-1,n-1

        while head:
            for j in range(y1, y2+1):
                if head:
                    grid[x1][j] = head.val
                    head = head.next
            x1 += 1

            for i in range(x1, x2+1):
                if head:
                    grid[i][y2] = head.val
                    head = head.next
            y2 -= 1

            for j in range(y2, y1 - 1, -1):
                if head:
                    grid[x2][j] = head.val
                    head = head.next
            x2 -= 1

            for i in range(x2, x1 - 1, -1):
                if head:
                    grid[i][y1] = head.val
                    head = head.next
            y1 += 1

        return grid
