class Solution {
public:
    int minimumDifference(vector<int>& nums) {
        int N = nums.size() / 2;
        int total = accumulate(nums.begin(), nums.end(), 0);
        int half = total / 2;
        int ans = abs(accumulate(nums.begin(), nums.begin() + N, 0) - accumulate(nums.begin() + N, nums.end(), 0));
        
        vector<vector<int>> left(N + 1), right(N + 1);
        for(int i = 0; i < (1 << N); ++i){
            int cnt = __builtin_popcount(i), sum = 0;
            for(int j = 0; j < N; ++j) if(i >> j & 1) sum += nums[j];
            left[cnt].push_back(sum);
            sum = 0;
            for(int j = 0; j < N; ++j) if(i >> j & 1) sum += nums[j + N];
            right[cnt].push_back(sum);
        }
        for(int k = 1; k < N; ++k){
            sort(right[N - k].begin(), right[N - k].end());
            for(auto &x : left[k]){
                auto it = lower_bound(right[N - k].begin(), right[N - k].end(), half - x);
                if(it != right[N - k].end()){
                    int left_ans_sum = x + *it;
                    int right_ans_sum = total - left_ans_sum;
                    ans = min(ans, abs(left_ans_sum - right_ans_sum));
                }
            }
        }
        return ans;
    }
};
