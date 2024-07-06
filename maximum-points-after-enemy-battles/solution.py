class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        a=min(enemyEnergies)
        if currentEnergy<a:
            return 0
        currentEnergy-=a
        total=sum(enemyEnergies)
        a=min(enemyEnergies)
        return 1+(currentEnergy+total-a)//a