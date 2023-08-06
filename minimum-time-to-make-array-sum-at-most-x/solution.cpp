class Solution {
public:
    vector<int> order;
    vector<vector<int>> dp;
    int n;
    vector<int> nums1, nums2;

    int dfs(int idx, int to_pick){
        if(idx == n || to_pick == 0){
            return 0;
        }
        if(dp[idx][to_pick] != -1){
            return dp[idx][to_pick];
        }
        int i = order[idx];
        int leave = dfs(idx + 1, to_pick);
        int take = nums1[i] + to_pick * nums2[i] + dfs(idx + 1, to_pick - 1);
        dp[idx][to_pick] = max(take, leave);
        return dp[idx][to_pick];
    }

    int minimumTime(vector<int>& A, vector<int>& B, int x) {
        n = A.size();
        nums1 = A;
        nums2 = B;
        dp.resize(n + 1, vector<int>(n + 1, -1));
        order.resize(n);

        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b){
            return nums2[a] > nums2[b];
        });

        int s1 = accumulate(nums1.begin(), nums1.end(), 0);
        int s2 = accumulate(nums2.begin(), nums2.end(), 0);
        for(int i = 0; i <= n; i++){
            int total = s1 + i * s2;
            if(total - dfs(0, i) <= x){
                return i;
            }
        }
        return -1;
    }
};
