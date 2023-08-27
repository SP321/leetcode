class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        cnt = Counter(nums)
        ans = 0
        i = 1
        while target > 0:
            lsb = target & -target
            while i < lsb:
                next_i = i * 2
                cnt[next_i] += cnt[i] // 2
                cnt[i] %= 2
                i = next_i
            if cnt[i] > 0:
                cnt[i] -= 1
                target -= i
            else:
                found = False
                next_i = i
                while next_i <= max(cnt.keys()):
                    if cnt[next_i] > 0:
                        cnt[next_i] -= 1
                        cnt[next_i // 2] += 2
                        ans += 1
                        found = True
                        break
                    next_i *= 2
                if not found:
                    return -1
        return ans