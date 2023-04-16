class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        sort(divisors.begin(),divisors.end(),greater<int>());
        int ma=0;
        int in=0;
        for(int i=0;i<divisors.size();i++){
            int c=0;
            for(int &x:nums){
                if(x%divisors[i]==0)
                    c++;
            }
            if(c>=ma){
                ma=c;
                in=i;
            }                
        }
        return divisors[in];
    }
};