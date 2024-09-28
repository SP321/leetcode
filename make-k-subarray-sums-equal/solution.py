class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)

        no_of_buckets = gcd (k, n)
        buckets = defaultdict(list)

        for ind, num in enumerate(arr):
            buckets[ind % no_of_buckets].append(num)

        result = 0
        for bucket_number, bucket in buckets.items():
            sorted_bucket = sorted(bucket)
            m = len(sorted_bucket)
            median = sorted_bucket[(m)//2]
            
            for num in bucket:
                result += abs(median - num)

        return result
