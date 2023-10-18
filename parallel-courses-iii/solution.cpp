class Solution {
public:
    unordered_map<int, vector<int>> graph;
    vector<int> time;
    vector<int> dp;

    int dfs(int i) {
        if (dp[i] != -1) {
            return dp[i];
        }
        
        int max_child_time = 0;
        for (int j : graph[i]) {
            max_child_time = max(max_child_time, dfs(j));
        }
        
        return dp[i] = max_child_time + time[i - 1];
    }

    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        this->time = time;
        dp.assign(n + 1, -1);

        for (const vector<int>& relation : relations) {
            int prev_course = relation[0];
            int next_course = relation[1];
            graph[prev_course].push_back(next_course);
        }

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            ans = max(ans, dfs(i));
        }

        return ans;
    }
};