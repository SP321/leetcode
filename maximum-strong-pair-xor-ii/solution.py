class TrieNode:
    def __init__(self):
        self.occurences=0
        self.children=[None]*2
BITLENGTH=20 
class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,num):
        cur=self.root
        for i in range(BITLENGTH,-1,-1):
            bit=num>>i&1
            if cur.children[bit]==None:
                cur.children[bit]=TrieNode()
            cur.children[bit].occurences+=1
            cur=cur.children[bit]
    
    def find(self,num):
        cur=self.root
        ans=0
        for i in range(BITLENGTH,-1,-1):
            bit=num>>i&1
            ans=ans<<1
            if cur.children[bit^1]!=None and cur.children[bit^1].occurences>0:
                ans+=1
                cur=cur.children[bit^1]
            else:
                cur=cur.children[bit]
        return ans
    
    def delete(self, num, i = 0):
        cur=self.root
        for i in range(BITLENGTH,-1,-1):
            bit=num>>i&1
            cur.children[bit].occurences-=1
            cur=cur.children[bit]
    
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        l=0
        trie=Trie()
        for r in range(n):
            trie.insert(nums[r])
            while abs(nums[r]-nums[l])>min(nums[r],nums[l]):
                trie.delete(nums[l])
                l+=1
            ans=max(ans,trie.find(nums[r]))
        return ans