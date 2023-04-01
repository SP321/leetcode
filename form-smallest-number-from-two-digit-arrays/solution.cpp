class Solution {
public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> a(11,vector<int>(2,0));
        for(int i=0;i<nums1.size();i++)
            a[nums1[i]][0]=1;
        for(int i=0;i<nums2.size();i++)
            a[nums2[i]][1]=1;
        for(int i=0;i<10;i++)
            if(a[i][0]&&a[i][1])
                return i;
        int x,y;
        for(int i=9;i>0;i--){
            if(a[i][0]==1)
                x=i;
            if(a[i][1]==1)
                y=i;
        }
        return min(x,y)*10+max(x,y);
    }
};