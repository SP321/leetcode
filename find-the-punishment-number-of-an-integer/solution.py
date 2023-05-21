class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition_string(input_string):
            def _partition(index, partitions):
                if index == len(input_string):
                    result.append([''.join(partition) for partition in partitions])
                    return
                _partition(index + 1, partitions + [[input_string[index]]])
                if partitions:
                    _partition(index + 1, partitions[:-1] + [partitions[-1] + [input_string[index]]])

            result = []
            _partition(0, [])
            return result
        ans=0
        for i in range(1,n+1):
            x=i*i
            for aa in partition_string(str(x)):
                 y=sum(int(i) for i in aa)
                 if i==y:
                    ans+=x
                    break
        return ans