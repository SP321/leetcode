class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        n = len(tasks)
        m = len(processorTime)
        ans = 0

        i = 0
        for j in range(m):
            currentEndTime = processorTime[j]
            if i < n:
                currentEndTime += tasks[i]
                i += 4
            ans = max(ans, currentEndTime)

        return ans