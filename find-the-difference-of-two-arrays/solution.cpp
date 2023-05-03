class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<int>a(2001);
        vector<int>b(2001);
        for(int i=0;i<nums1.size();i++)
            a[1000+nums1[i]]=1;
        for(int i=0;i<nums2.size();i++)
            b[1000+nums2[i]]=1;
        vector<vector<int>>ans(2,vector<int>());
        for(int i=0;i<2001;i++){
            if(a[i]&& !b[i])
                ans[0].push_back(i-1000);
            if(b[i]&& !a[i])
                ans[1].push_back(i-1000);
        }
        return ans;
    }
};