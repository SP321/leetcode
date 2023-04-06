class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        map<int,int>m;
        for(int i=0;i<nums.size();i++){
            if(m[nums[i]]){
                nums.erase(nums.begin()+i--);
                continue;
            }
            m[nums[i]]=1;
        }
        return nums.size();
    }
};