class Solution {
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        int n=plantTime.size();
        vector<int>o(n);
        for(int i=0;i<n;i++)
            o[i]=i;
        sort(o.begin(),o.end(),[&plantTime,&growTime](int x,int y){
            if (growTime[x]==growTime[y])
                return plantTime[x]<plantTime[y];
            return growTime[x]>growTime[y];
        });
        int ans=0;
        int acc=0;
        for(int i=0;i<n;i++){
            acc+=plantTime[o[i]];
            ans=max(ans,acc+growTime[o[i]]);
        }
        return ans;
    }
};