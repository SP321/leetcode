class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        n=len(prices)
        for i in range(n-1,-1,-1):
            while st and prices[i] < st[-1]:
                st.pop()
            temp=prices[i]
            if st:
                prices[i]-=st[-1]
            st.append(temp)
        return prices