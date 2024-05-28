class Solution {
public:
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        unordered_map<int,vector<int>>g;
        for(auto &p:richer){
            g[p[1]].push_back(p[0]);
        }
        unordered_map<int,int>memo;
        function<int(int)> dfs=[&](int x){
            if (memo.find(x)!=memo.end())
                return memo[x];
            int ans=x;
            for(int &nei:g[x]){
                int y=dfs(nei);
                if(quiet[y]<quiet[ans])
                    ans=y;
            }
            return memo[x]=ans;
        };
        vector<int>ans;
        for(int i=0;i<quiet.size();i++){
            ans.push_back(dfs(i));
        }
        return ans;
    }
};