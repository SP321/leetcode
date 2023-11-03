class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        j=1
        for i in target:
            while j<i:
                ans.append("Push")
                ans.append("Pop")
                j+=1
            j+=1
            ans.append("Push")
        return ans