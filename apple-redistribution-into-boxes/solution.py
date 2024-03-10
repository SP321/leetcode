class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        x=sum(apple)
        ans=0
        capacity.sort(reverse=True)
        for y in capacity:
            x-=y
            ans+=1
            if x<=0:
                return ans
        
        