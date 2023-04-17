class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        map<int,int>c;
        for(int &x:nums)
            c[x]=1;
        int ans=0;
        for(auto p:c){
            int x=p.first;
            if(c[x-1]==0){
                int j=1;
                while(c[x+j])
                    j++;
                ans=max(ans,j);
            }
        }
        return ans;
    }
};