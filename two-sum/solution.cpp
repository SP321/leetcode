class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l=0,h=nums.size()-1;
        vector<int>order;
        for(int i=0;i<nums.size();i++)
            order.push_back(i);
        sort(order.begin(),order.end(),[&nums](int a,int b){return nums[a]<nums[b];});
        while(l<h){
            if(nums[order[l]]+nums[order[h]]>target)
                h--;
            else if (nums[order[l]]+nums[order[h]]<target)
                l++;
            else
                return {order[l],order[h]};
        }
        return {};
    }
};