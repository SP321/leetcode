class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(),points.end(),[](vector<int>a,vector<int>b){return a[1]<b[1];});
        long reach=LONG_MIN;
        int ans=0;
        for(auto &x:points){
            if(x[0]>reach){
                reach=x[1];
                ans+=1;
            }
        }
        return ans;
    }
};