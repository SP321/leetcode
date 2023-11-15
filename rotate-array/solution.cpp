class Solution {
public:

    void rotate(vector<int>& nums, int k) {
        #define rev(a,b) reverse(nums.begin()+(a),nums.begin()+(b));
    
        k %= nums.size();
        int i,j;
        if (k > 0){
            rev(0,nums.size())
            rev(0,k)
            rev(k,nums.size())
        }
    }
};