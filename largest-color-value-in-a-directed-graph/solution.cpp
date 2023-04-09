class Solution {
public:
    string c;
    vector<vector<int>> next, prev, counts;
    vector<int> saved;
    vector<int> seen;
    
    int dfs(int x) {
        if(seen[x])
            return -1;
        if (saved[x] != -1)
            return saved[x];
        seen[x]=1;
        int max_count = -1;
        for (int y : next[x]) {
            int result = dfs(y);
            if (result == -1){
                seen[x]=0;
                return -1;
            }
            for (int i = 0; i < 26; i++) 
                counts[x][i] = max(counts[x][i], counts[y][i]);
            max_count = max(max_count, result);
        }
        counts[x][c[x] - 'a']++;
        max_count = max(max_count, counts[x][c[x] - 'a']);
        saved[x] = max_count;
        seen[x]=0;
        return max_count;
    }
    
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        c = colors;
        prev.resize(n);
        next.resize(n);
        seen.resize(n);
        counts.resize(n, vector<int>(26, 0));
        saved.resize(n, -1);
        for (auto& edge : edges) {
            next[edge[0]].push_back(edge[1]);
            prev[edge[1]].push_back(edge[0]);
        }
        int ans = -1;
        for (int i = 0; i < n; i++) {
            int result = dfs(i);
            if (result == -1)
                return -1;
            ans = max(ans, result);
        }
        return ans;
    }
};