class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> ans;
        for(auto &x : nums){
            string num = to_string(x);
            for(auto &st : num){
                ans.push_back(st-'0');
            }
        }
        return ans;
    }
};