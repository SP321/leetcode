class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False

        s_list = [int(ch) for ch in reversed(s)]
        count_reachable = 0
        i = 0
        windowsize = maxJump - minJump + 1
        
        s_list[0] = 2
        
        for j in range(0, n):
            if s_list[j] == 2:
                count_reachable += 1
                
            while i <= j - windowsize:
                if s_list[i] == 2:
                    count_reachable -= 1
                i += 1

            parent = j + minJump
            if parent >= n:
                continue

            if count_reachable == 0:
                s_list[parent] = 1
            elif s_list[parent] == 0:
                s_list[parent] = 2

        return s_list[-1] == 2
