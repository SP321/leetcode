class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        to_ban_d=0
        to_ban_r=0
        cr=senate.count('R')
        cd=senate.count('D')
        banned=set()
        while True:
            for i in range(len(senate)):
                if i in banned:
                    continue
                if senate[i]=='D':
                    if to_ban_d>0:
                        to_ban_d-=1
                        banned.add(i)
                        cd-=1
                    else:
                        to_ban_r+=1
                if senate[i]=='R':
                    if to_ban_r>0:
                        to_ban_r-=1
                        banned.add(i)
                        cr-=1
                    else:
                        to_ban_d+=1
                if cr<=to_ban_r:
                    return 'Dire'
                if cd<=to_ban_d:
                    return 'Radiant'