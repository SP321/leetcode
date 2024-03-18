class Solution {
public:
    int minimizeConcatenatedLength(vector<string>& v) {
        if (v.empty()) return 0;
        typedef tuple<int,int,int> key;
        map<key,int>dp;

        function<int(int, int, int)> dfs = [&](int i, int start, int end) -> int {
            if(i >= v.size()) return 0;
            key cur_key={i,start,end};
            if(dp.find(cur_key) != dp.end()) return dp[cur_key];
            return dp[cur_key] = min(
                (int)v[i].size() - (end + 'a' == v[i][0]) + dfs(i + 1, start, v[i].back() - 'a'),
                (int)v[i].size() - (start + 'a' == v[i].back()) + dfs(i + 1, v[i][0] - 'a', end)
            );
        };
        
        return v[0].size() + dfs(1, v[0][0] - 'a', v[0].back() - 'a');
    }
};