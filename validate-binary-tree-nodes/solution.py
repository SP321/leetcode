class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        q = deque()
        q.append(0)
        visited = defaultdict(bool)

        for i in range(n):
            if leftChild[i] == q[0] or rightChild[i] == q[0]:
                q.append(i)
                q.popleft()

        while q:
            node = q.popleft()
                
            if visited[node]: 
                return False
            
            n -= 1
            visited[node] = True
            
            if leftChild[node] != -1:
                q.append(leftChild[node])
            if rightChild[node] != -1:
                q.append(rightChild[node])
        
        return n == 0