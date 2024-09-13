class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr=list(accumulate(arr,lambda x,y:x^y,initial=0))
        return [arr[r+1] ^ arr[l] for l,r in queries]