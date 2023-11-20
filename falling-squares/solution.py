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

    def _build(self, idx):
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def query(self, start, stop):
        start += self._size
        stop += self._size
        self._update_node(start)
        self._update_node(stop - 1)
        res = self._default
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
            return self.query(idx.start,idx.stop)
        else:
            return self.query(idx, idx+1)

    def __setitem__(self, idx, value):
        if isinstance(idx, slice):
            self.update_range(idx.start,idx.stop,value )
        else:
            self.update_range(idx,idx+1, value)

    def update_range(self, start, stop, value):
        # This method should be implemented in the derived classes
        raise NotImplementedError("This method should be implemented in the derived class")


class LazyAssignSegmentTree(BaseSegmentTree):
    def __init__(self, data, default=0, func=max):
        super().__init__(data, default, func)
        self._lazy = [None] * (2 * self._size)

    def _push(self, idx):
        # Push the lazy value down to children
        if self._lazy[idx] is not None:
            # Propagate the lazy value to the children and update their values
            self.data[idx * 2] = self._lazy[idx]
            self.data[idx * 2 + 1] = self._lazy[idx]
            self._lazy[idx * 2] = self._lazy[idx]
            self._lazy[idx * 2 + 1] = self._lazy[idx]
            self._lazy[idx] = None

    def _update_node(self, idx):
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def update_range(self, start, stop, value):
        self._update(1, 0, self._size - 1, start, stop-1, value)

    def _update(self, idx, start, end, l, r, value):
        if l > r:
            return
        if l == start and r == end:
            # Assign the value and set the lazy value
            self.data[idx] = value
            self._lazy[idx] = value
        else:
            # Propagate lazy value if necessary
            self._push(idx)
            mid = (start + end) // 2
            # Recursively update left and right children
            self._update(idx * 2, start, mid, l, min(r, mid), value)
            self._update(idx * 2 + 1, mid + 1, end, max(l, mid + 1), r, value)
            # Update the current node
            self.data[idx] = self._func(self.data[idx * 2], self.data[idx * 2 + 1])



    def __setitem__(self, idx, value):
        if isinstance(idx, slice):
            self.update_range(idx.start,idx.stop,value)
        else:
            self.update_range(idx,idx+1, value)

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        s=set()
        for x,a in positions:
            s.add((x,0))
            s.add((x,1))
            s.add((x+a,0))
            s.add((x+a,1))
        d={}
        index=0
        for i in sorted(s):
            d[i]=index
            index+=1
        st=LazyAssignSegmentTree([0]*len(d),default=0)

        ans=[]
        ma=0

        for x,a in positions: 
            cur_h = st[d[(x,1)]:d[(x+a,0)]]+a 
            st[d[(x,1)]:d[(x+a,0)]]=cur_h
            ma=max(ma,cur_h)
            ans.append(ma)
        return ans
