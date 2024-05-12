class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n=len(energy)
        for i in range(k,n):
            energy[i]=max(energy[i-k]+energy[i],energy[i])
        return max(energy[-k:])