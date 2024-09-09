class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = {}
        arr = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

        for i in range(len(arr)):
            for j in arr[i]:
                d[j] = i+1

        ans = []

        for i in words:
            prev = 0
            flag = 1
            cp = i
            i = i.lower()
            
            for j in i:
                if prev == 0:
                    prev = d[j]
                else:
                    if prev != d[j]:
                        flag = 0
                        break
            if flag:
                ans.append(cp)

        return ans