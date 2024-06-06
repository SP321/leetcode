class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        unordered_map<int,int>c;
        for(int &x:hand){
            c[x]+=1;
        }
        sort(hand.begin(),hand.end());
        for(int &x:hand){
            if(c[x])
                for(int j=x;j<x+groupSize;j++){
                    if(c[j])
                        c[j]-=1;
                    else
                        return 0;
                }
        }
        return 1;
    }
};