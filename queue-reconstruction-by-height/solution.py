#Sandeep Polamuri

class BaseSegmentTree:
    def __init__(self, data, default=0, func=max):
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"

    def _push(self, idx):
        # This method should be implemented in the derived classes
        raise NotImplementedError("This method should be implemented in the derived class")

    def _update_node(self, idx):
        # This method should be implemented in the derived classes
        raise NotImplementedError("This method should be implemented in the derived class")

    def _update_tree(self, idx):
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def query(self, start, stop, default=0):
        start += self._size
        stop += self._size
        self._update_node(start)
        self._update_node(stop - 1)
        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            start = idx.start
            stop = idx.stop
        else:
            start = idx
            stop = idx + 1
        return self.query(start, stop)

    def __setitem__(self, idx, value):
        if isinstance(idx, slice):
            start = idx.start
            stop = idx.stop
        else:
            start = idx
            stop = idx + 1
        self.update_range(start, stop, value)

    def update_range(self, start, stop, value):
        # This method should be implemented in the derived classes
        raise NotImplementedError("This method should be implemented in the derived class")


class LazyAddSegmentTree(BaseSegmentTree):
    def __init__(self, data, default=0, func=max):
        super().__init__(data, default, func)
        self._lazy = [0] * (2 * self._size)

    def _push(self, idx):
        q, self._lazy[idx] = self._lazy[idx], 0
        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update_node(self, idx):
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def update_range(self, start, stop, value):
        self.add(start, stop, value)

    def add(self, start, stop, value):
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1
        self._update_tree(start_copy)
        self._update_tree(stop_copy - 1)


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        st = LazyAddSegmentTree(list(range(n)), default=0, func=lambda x, y: x+y )
        ans = [None] * n
        for h, k in sorted(people,key=lambda x: (x[0], -x[1])):
            pos = bisect.bisect_right(st,k) - 1 
            ans[pos] = [h, k]
            if pos+1<n:
                st[pos+1:n] = -1
        return ans

