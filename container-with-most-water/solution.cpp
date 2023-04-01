class Solution {
public:
    int maxArea(vector<int>& height) {
        const int n=height.size();
        int lhi=0;
        int rhi=n-1;
        int ans=0;
        int i=0;
        int j=n-1;
        while(i<j){
            ans=max(ans,(rhi-lhi)*min(height[lhi],height[rhi]));
            if(height[i]>height[lhi]){
                lhi=i;
                ans=max(ans,(rhi-lhi)*min(height[lhi],height[rhi]));
            }
            if(height[j]>height[rhi]){
                rhi=j;
                ans=max(ans,(rhi-lhi)*min(height[lhi],height[rhi]));
            }
            if(height[rhi]==height[lhi]){
                i++;j--;
            }            
            else if(height[rhi]>height[lhi])
                i++;
            else
                j--;
        }
        return ans;
    }
};