class Solution {
public:
    string predictPartyVictory(string senate) {
        int br=0;
        int bd=0;
        int cr=0;
        int cd=0;
        int n=senate.size();
        for(int i=0;i<n;i++)
            if(senate[i]=='D')
                cd++;
            else
                cr++;
        while(1)
            for(int i=0;i<n;i++){
                if(senate[i]=='D'){
                    if(bd>0){
                        senate[i]='X';
                        bd--;
                        cd--;
                    }
                    else{
                        br++;
                    }
                }
                if(senate[i]=='R'){
                    if(br>0){
                        senate[i]='X';
                        br--;
                        cr--;
                    }
                    else{
                        bd++;
                    }
                }
                if(cr<br)
                    return "Dire";
                if(cd<bd)
                    return "Radiant";
            }
    
    }
};