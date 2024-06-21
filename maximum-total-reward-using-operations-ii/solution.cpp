class Solution {
public:
    int maxTotalReward(vector<int>& rewardValues) {
        set<int> uniqueRewards(rewardValues.begin(), rewardValues.end());
        vector<int> rewards(uniqueRewards.begin(), uniqueRewards.end());
        if (rewards.size() == 1) {
            return rewards[0];
        }

        vector<bool> mask(rewards.back() + 1, false);
        for (int x : rewards) {
            mask[x] = true;
        }

        function<bool(int, int, int)> dfs = [&](int idx, int cursum, int target) -> bool {
            if (target - cursum >= rewards[idx + 1]) {
                return false;
            }
            if (mask[target - cursum]) {
                return true;
            }
            for (int i = idx; i >= 0; --i) {
                if (cursum + rewards[i] <= target) {
                    mask[cursum + rewards[i]] = true;
                    if (dfs(i - 1, cursum + rewards[i], target)) {
                        return true;
                    }
                }
            }
            return false;
        };

        int n = rewards.size();
        for (int x = rewards[n - 1] - 1; x >= rewards[n - 2]; --x) {
            if (mask[x] || dfs(n - 2, 0, x)) {
                return rewards[n - 1] + x;
            }
        }
        return rewards[n - 1];
    }
};