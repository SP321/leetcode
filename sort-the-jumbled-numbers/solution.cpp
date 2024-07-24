class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        function<int(int)> convert = [&](int num) {
            string x=to_string(num);
            int ans=0;
            for(char ch:x){
                ans=ans*10+mapping[ch-'0'];
            }
            return ans;
        };
        sort(nums.begin(), nums.end(), [&](int a, int b) {
            return convert(a) < convert(b);
        });
        
        return nums;
    }
};