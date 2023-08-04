class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        map<int,int>d;
        for(auto &p:nums1){
            d[p[0]]+=p[1];
        }
        for(auto &p:nums2){
            d[p[0]]+=p[1];
        }
        vector<vector<int>>ans;
        for(auto &i:d)
            ans.push_back({i.first,i.second});
        return ans;
    }
};