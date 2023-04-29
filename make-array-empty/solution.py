class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    def _lsb(self, i):
        return i & -i
    def update(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += self._lsb(i)
    def prefix_sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= self._lsb(i)
        return total
    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)
    def print_elements(self):
        elements = []
        for i in range(1, self.size + 1):
            elements.append(self.prefix_sum(i) - self.prefix_sum(i - 1))
        print(elements)
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n=len(nums)
        a=[i for i in range(n)]
        a.sort(key=lambda x:nums[x])
        count_op = FenwickTree(n)
        for i in range(n):
            count_op.update(i+1,1)
        ans=0
        curpos=0
        for i in a:
            move=0
            if i<curpos:
                move+=count_op.range_sum(curpos+1,n)
                move+=count_op.range_sum(0,i+1)
            else:
                move+=count_op.range_sum(curpos+1,i+1)
            ans+=move
            count_op.update(i+1,-1) 
            curpos=i
        return ans