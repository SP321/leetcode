class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr=[[a,'a'],[b,'b'],[c,'c']]
        ans=[]
        while True:
            arr.sort(reverse=True)
            for i in range(3):
                if arr[i][0]>0 and ans[-2:]!=[arr[i][1],arr[i][1]]:
                    ans.append(arr[i][1])
                    arr[i][0]-=1
                    break
            else:
                break
        return ''.join(ans)
        
