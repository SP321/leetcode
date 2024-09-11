class Solution {
public:
    int minBitFlips(int start, int goal) {
        int ans=0;
        start^=goal;
        while(start){
            ans+=1;
            start=start&(start-1);
        }
        return ans;
    }
};