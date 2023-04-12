class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int closest=1e5;
        int temp;
        for(int i=0;i<nums.size();i++){
            int l=i+1;
            int h=nums.size()-1;
            while(l<h){
                temp=nums[i]+nums[l]+nums[h];
                if(abs(temp-target)<abs(closest-target))
                    closest=temp;
                if(temp>=target)
                    h--;
                if(temp<=target)
                    l++;
            }
        }
        return closest;
    }
};