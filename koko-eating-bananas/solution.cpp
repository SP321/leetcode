class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int i=1;
        int j=1e9;
        int ans=j;
        while(i<=j){
            long long hoursum=0;
            int m=i+(j-i)/2;
            for(auto &x:piles)
                hoursum+=(x+m-1)/m;
            if(hoursum>h)
                i=m+1;
            else{
                ans=m;
                j=m-1;
            }
        }
        return ans;
    }
};