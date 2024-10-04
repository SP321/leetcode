class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int n=skill.size();
        vector<int>cnt(1001,0);
        int mn=1001,mx=0;
        for(auto &x:skill){
            mx=max(mx,x);
            mn=min(mn,x);
            cnt[x]+=1;
        }
        int target=mn+mx;
        long long ans=0;
        int c=0;
        for(int i=0;i<1001;i++){
            if(cnt[i]){
                int j=target-i;
                if(cnt[i]!=cnt[j])
                    return -1;
                ans+=1ll*i*j*cnt[i];
            }
        }
        return ans/2;
    }
};
auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();