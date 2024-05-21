class Solution {
public:
    long long sumDigitDifferences(vector<int>& nums) {
        long long ans = 0;
        vector<vector<int>> freq(10, vector<int>(10, 0));
        for(auto n: nums){
            for(int i = 0; n > 0; n = n/10, i++) freq[i][n%10]++;
        }
        for(int i = 0; i < freq.size(); ++i){
            for(int j = 0; j < freq[0].size(); ++j) ans += freq[i][j] * ( nums.size() - freq[i][j]);
        }
        return ans/2;
    }
};