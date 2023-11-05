class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int ans=0;
        for(int &i:left)
            ans=max(i,ans);
        for(int &i:right)
            ans=max(n-i,ans);
        return ans;
    }
};