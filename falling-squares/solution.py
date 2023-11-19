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



class LazyAssignSegmentTree(BaseSegmentTree):
    def __init__(self, data, default=0, func=max):
        super().__init__(data, default, func)
        self._lazy = [None] * (2 * self._size)

    def _push(self, idx):
        if self._lazy[idx] is not None:
            self.data[idx * 2] = self.data[idx * 2 + 1] = self._lazy[idx]
            self._lazy[idx * 2] = self._lazy[idx * 2 + 1] = self._lazy[idx]
            self._lazy[idx] = None

    def _update_node(self, idx):
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def update_range(self, start, stop, value):
        self._update(1, 0, self._size - 1, start, stop, value)

    def _update(self, idx, tl, tr, l, r, new_val):
        if l > r:
            return
        if l == tl and r == tr:
            self.data[idx] = new_val
            self._lazy[idx] = new_val
        else:
            self._push(idx)
            tm = (tl + tr) // 2
            self._update(idx * 2, tl, tm, l, min(r, tm), new_val)
            self._update(idx * 2 + 1, tm + 1, tr, max(l, tm + 1), r, new_val)
            self.data[idx] = self._func(self.data[idx * 2], self.data[idx * 2 + 1])

    def __setitem__(self, idx, value):
        if isinstance(idx, slice):
            start = idx.start
            stop = idx.stop
        else:
            start = idx
            stop = idx + 1
        self.update_range(start, stop, value)



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


class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
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

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
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

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

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

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)
    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            start=idx.start
            stop=idx.stop
        else:
            start=idx
            stop=idx+1
        return self.query(start,stop)

    def __setitem__(self, idx, value):
        if isinstance(idx, slice):
            start=idx.start
            stop=idx.stop
        else:
            start=idx
            stop=idx+1
        self.add(start,stop,value)


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
