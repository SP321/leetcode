class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& t) {
        stack<int>x;
        int n=t.size();
        vector<int>ans(n);
        for(int i=0;i<n;i++){
            while(x.size() and t[i]>t[x.top()]){
                ans[x.top()]=i-x.top();
                x.pop();
            }
            x.push(i);
        }
        return ans;
    }
};