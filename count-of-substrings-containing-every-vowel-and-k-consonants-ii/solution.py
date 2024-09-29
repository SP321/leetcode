vowel=[ True if x in "aeiou" else False for x in ascii_lowercase]
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        arr=[ord(x)-ord('a') for x in word]
        def helper(k):
            ans = 0
            i = 0
            vcnt=[0]*26
            v=0
            c=0
            for j in range(n):
                x=arr[j]
                if vowel[x]:
                    if vcnt[x]==0:
                        v+=1
                    vcnt[x]+=1
                else:
                    c+=1
                while v==5 and c>k:
                    x=arr[i]
                    if vowel[x]:
                        vcnt[x]-=1
                        if vcnt[x]==0:
                            v-=1
                    else:
                        c-=1
                    i += 1
                ans += (j - i + 1)
            return ans

        return helper(k) - helper(k - 1)