class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int dsum = 0, esum = 0;
        for(auto n: nums){
            esum += n;
            while(n > 0){
                dsum += n%10;
                n = n/10;
            }
        }
        return esum - dsum;
    }
};