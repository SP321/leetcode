class Solution {
private:
    map<string, vector<pair<string, double>>> adjList;
    map<string, bool> seen;

public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        for (int i = 0; i < equations.size(); i++) {
            string x = equations[i][0], y = equations[i][1];
            double value = values[i];

            adjList[x].push_back({y, value});
            adjList[y].push_back({x, 1.0 / value});
        }

        vector<double> results;
        for (auto& query : queries) {
            for (auto& node : adjList) {
                seen[node.first] = false;
            }
            double result = dfs(query[0], query[1], 1.0);
            results.push_back(result);
        }
        return results;
    }

    double dfs(string i, string j, double prod) {
        if (seen.find(i) == seen.end() || seen.find(j) == seen.end() || seen[i]) {
            return -1.0;
        }
        seen[i] = true;

        if (i == j) {
            return prod;
        }

        double ans = -1.0;
        if (adjList.find(i) != adjList.end()) {
            for (auto& node : adjList[i]) {
                ans = max(ans, dfs(node.first, j, prod * node.second));
            }
        }
        return ans;
    }
};