class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        map<int,int>c;
        for(int &i:nums)
            c[i]++;
        vector<int>ans;
        for(auto &p:c)
            if(p.second>nums.size()/3)
                ans.push_back(p.first);
        return ans;
    }
};