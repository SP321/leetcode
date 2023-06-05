class Solution {
public:
    void dfs(vector<int>& candidates, int target, vector<int>& combination, int start, vector<vector<int>>& results) {
        if (target == 0) {
            results.push_back(combination);
            return;
        } else if (target < 0) {
            return;
        }
        for (int i = start; i < candidates.size(); ++i) {
            combination.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], combination, i, results);
            combination.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> results;
        vector<int> combination;
        dfs(candidates, target, combination, 0, results);
        return results;
    }
};