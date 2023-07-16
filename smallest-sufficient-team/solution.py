class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        skill_dict = {req_skills[i]: i for i in range(n)}
        m = len(people)
        dp = [0] + [float('inf')] * ((1 << n) - 1)
        team = [()] + [()] * ((1 << n) - 1)
        people_skills = [0] * m
        for i, p in enumerate(people):
            for s in p:
                if s in skill_dict:
                    people_skills[i] |= (1 << skill_dict[s])
        for i, ps in enumerate(people_skills):
            for skill_set in range(1 << n):
                if (skill_set | ps) != skill_set:
                    if 1 + dp[skill_set] < dp[skill_set | ps]:
                        dp[skill_set | ps] = 1 + dp[skill_set]
                        team[skill_set | ps] = team[skill_set] + (i,)
        return team[(1 << n) - 1]