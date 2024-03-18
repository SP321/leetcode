class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        sort(logs.begin(),logs.end(),[](auto a,auto b){return a[1]<b[1];});
        int m=queries.size();
        vector<int> ans(m);
        map<int,int>mp;
        int c=n;
        vector<int> order(m);
        for(int i=0;i<m;i++){
            order[i]=i;
        }
        sort(order.begin(),order.end(),[&queries](int a,int b){return queries[a]<queries[b];});
        int i=0,j=0;
        for(int k=0;k<m;k++){
            int cur=order[k];
            int t=queries[cur];
            while (j < logs.size() and logs[j][1] <= t){
                mp[logs[j][0]] += 1;
                if(mp[logs[j][0]]==1)
                    c-=1;
                j += 1;
            }
            while (i < logs.size() and logs[i][1] < t - x){
                mp[logs[i][0]] -= 1;
                if(mp[logs[i][0]] == 0)
                    c+=1;
                i += 1;
            }
            cout<<ans.size()<<" "<<cur<<endl;
            ans[cur] =c;
        }
        return ans;
    }
};