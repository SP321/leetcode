class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int ans=0,cur=0;
        unordered_map<int,int>c;
        c[0]=1;
        for(int &x:nums){
            cur+=x;
            cur=((cur%k)+k)%k;
            cout<<cur<<" "<<c[cur]<<" "<<ans<<endl;
            ans+=c[cur];
            c[cur]+=1;
        }
        return ans;
    }
};