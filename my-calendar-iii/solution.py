class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.value = 0
        self.node_count = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, n, default=0,func=max):
        self.root = SegmentTreeNode(0, n)
        self._default = default
        self._func=func

    def __update(self, node, start, end, value, updatefunc):
        if start <= node.start and end >= node.end:
            node.node_count += 1
            node.value = updatefunc(node.value,value)
            return
        if start > node.end or end < node.start:
            return
        if not node.left:
            node.left = SegmentTreeNode(node.start, node.mid)
            node.right = SegmentTreeNode(node.mid + 1, node.end)
        self.__update(node.left, start, end,value,updatefunc)
        self.__update(node.right, start, end,value,updatefunc)
        node.value = self._func(node.left.value, node.right.value) + node.node_count

    def __query(self, node, start, end):
        if node is None or start > node.end or end < node.start:
            return self._default
        if start <= node.start and end >= node.end:
            return node.value
        return self._func(self.__query(node.left, start, end), self.__query(node.right, start, end))

    def update(self, start, end, value, updatefunc=lambda x, y: x + y):
        self.__update(self.root, start, end-1, value, updatefunc)

    def query(self, start, end):
        return self.__query(self.root, start, end-1)

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
        if isinstance(value, tuple) and callable(value[0]):
            self.update(start,stop, value[1],updatefunc=value[0])
        else:
            self.update(start,stop,value, lambda x,y:y)

class MyCalendarThree:
    def __init__(self):
        self.tree = SegmentTree(10 ** 9,default=0,func=max)

    def book(self, startTime: int, endTime: int) -> int:
        self.tree[startTime:endTime]=(lambda x,y:x+y,1)
        return self.tree.root.value