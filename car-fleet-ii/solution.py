class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        st = []
        n = len(cars)
        ans = [-1] * n
        for i in range(n-1, -1, -1):
            p, s = cars[i]
            while st and (s <= cars[st[-1]][1] or (cars[st[-1]][0] - p) / (s - cars[st[-1]][1]) >= ans[st[-1]] > 0):
                st.pop()
            if st:
                ans[i] = (cars[st[-1]][0] - p) / (s - cars[st[-1]][1])
            st.append(i)
        return ans