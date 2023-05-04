class NumArray {
public:
    vector<int>prefsum;
    NumArray(vector<int>& nums) {
        int n=nums.size();
        prefsum.resize(n+1);
        for(int i=0;i<n;i++)
            prefsum[i+1]=prefsum[i]+nums[i];
    }

    int sumRange(int left, int right) { 
        return prefsum[right+1]-prefsum[left];   
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */