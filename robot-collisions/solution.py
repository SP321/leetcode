class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted((pos, health, dir, i) for i, (pos, health, dir) in enumerate(zip(positions, healths, directions)))
        stack = [] 
        for pos, health, dir, i in robots:
            if dir == 'R':
                stack.append((health, dir, i))
            else:
                while stack and stack[-1][1] == 'R':
                    if stack[-1][0] < health:
                        stack.pop()
                        health-=1
                    elif stack[-1][0] > health:
                        stack[-1] = (stack[-1][0] - 1, stack[-1][1], stack[-1][2])
                        health=0
                        break
                    else:
                        stack.pop()
                        health=0
                        break
                if health>0:
                    stack.append((health, dir, i))
        return [health for health, dir, i in sorted(stack, key=lambda x: x[2])]