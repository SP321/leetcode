class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> c;
        for (int num : nums) {
            c[num]++;
        }
        
        sort(nums.begin(), nums.end(), [&](int a, int b) {
            if (c[a] == c[b]) {
                return a > b;
            }
            return c[a] < c[b];
        });
        
        return nums;
    }
};