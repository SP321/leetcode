class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        if isinstance(data, int):
            self._len = data
            self._size = _size = 1 << (self._len - 1).bit_length()
            self.data = [default] * (2 * _size)
        else:
            self._len = len(data)
            self._size = _size = 1 << (self._len - 1).bit_length()
            self.data = [default] * (2 * _size)
            self.data[_size:_size + self._len] = data
            for i in reversed(range(_size)):
                self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        if isinstance(idx, slice): return self.query(idx.start,idx.stop)
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

from sortedcontainers import SortedList
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        a = SortedList([0])
        b = SegmentTree(50000)
        ans = []
        for q in queries:
            if q[0] == 1:
                val=q[1]
                pos = a.bisect_left(val)
                prev_value=a[pos-1]
                if pos < len(a):
                    next_value= a[pos]
                    b[next_value]=(next_value-prev_value)-(val-prev_value)
                b[val]=val-prev_value
                a.add(val)
            elif q[0] == 2:
                _, x, y = q
                max_distance = max(x-a[a.bisect_left(x)-1],b[0:x+1]) #segtree[l:r] queries [l,r)
                ans.append(max_distance >= y)
        return ans