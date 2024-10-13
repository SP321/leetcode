class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        int n=nums.size();
        
        unordered_map<int,int>c;
        set<pair<int,int>>left;
        set<pair<int,int>>right;
        long long cnt=0;

        auto add0=[&](int ct,int v){
            right.insert(make_pair(ct,v));
            cnt+=1ll*ct*v;
            if(right.size()>x){
                auto mn=*right.begin();
                cnt-=1ll*mn.first*mn.second;
                left.insert(mn);
                right.erase(right.begin());
            }
        };
        
        auto discard0=[&](int ct,int v){
            auto mn=*right.begin();
            auto cur=make_pair(ct,v);
            if(cur>=mn){
                cnt-=1ll*ct*v;
                right.erase(cur);
                if(left.size() and right.size()<x){
                    auto mx=*left.rbegin();
                    cnt+=1ll*mx.first*mx.second;
                    right.insert(mx);
                    left.erase(left.find(mx));
                }
            }
            else{
                left.erase(cur);
            }
        };

        auto add=[&](int x){
            if(c[x]>0)
                discard0(c[x],x);
            c[x]+=1;
            add0(c[x],x);
        };

        auto discard=[&](int x){
            discard0(c[x],x);
            c[x]-=1;
            if(c[x]>0)
                add0(c[x],x);
        };

        vector<long long>ans;
        int i=0;
        for(int j=0;j<n;j++){
            add(nums[j]);
            if(j-i+1>k){
                discard(nums[i]);
                i+=1;
            }
            if(j-i+1==k)
                ans.push_back(cnt);
        }
        return ans;
    }
};