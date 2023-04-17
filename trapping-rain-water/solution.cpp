class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        int x=0;
        vector<int>lwall(n);
        for(int i=0;i<n;i++){
            x=max(x,height[i]);
            lwall[i]=x;
        }
        vector<int>rwall(n);
        x=0;
        for(int i=n-1;i>=0;i--){
            x=max(x,height[i]);
            rwall[i]=x;
        }
        int i=0;
        int ans=0;
        while(i<n){
            int waterheight=min(lwall[i],rwall[i]);
            while(height[i]<waterheight)
                ans+=waterheight-height[i++];
            i++;
        }
        return ans;
    }
};