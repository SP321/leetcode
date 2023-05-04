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
    def update_value(self,i,value):
        old_value = self.prefix_sum(i) - self.prefix_sum(i - 1)
        delta = value - old_value
        self.update(i, delta)
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

class NumArray:
    def __init__(self, nums: List[int]):
        self.ft=FenwickTree(len(nums))
        for i in range(len(nums)):
            self.ft.update(i+1,nums[i])

    def update(self, index: int, val: int) -> None:
            self.ft.update_value(index+1,val)

    def sumRange(self, left: int, right: int) -> int:
            return self.ft.range_sum(left+1,right+1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)