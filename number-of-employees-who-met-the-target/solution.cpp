class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int ans=0;
        for(int &i:hours)
            ans+=i>=target;
        return ans;
    }
};