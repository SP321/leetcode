class Solution {
public:
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        set<int>x;
        for(int i=0;i<n;i++)
            x.insert(i);
        vector<int>ans;
        for(auto &q:queries){
            int u=q[0],v=q[1];
            auto st=x.lower_bound(u+1);
            auto end=x.lower_bound(v);
            x.erase(st,end);
            ans.push_back(x.size()-1);
        }
        return ans;
    }
};