vector<int> manacher_odd(string s) {
    int n = s.size();
    s = "$" + s + "^";
    vector<int> p(n + 2);
    int l = 1, r = 1;
    for(int i = 1; i <= n; i++) {
        p[i] = max(0, min(r - i, p[l + (r - i)]));
        while(s[i - p[i]] == s[i + p[i]]) {
            p[i]++;
        }
        if(i + p[i] > r) {
            l = i - p[i], r = i + p[i];
        }
    }
    return vector<int>(begin(p) + 1, end(p) - 1);
}
vector<int> manacher(string s) {
    string t;
    for(auto c: s) {
        t += string("#") + c;
    }
    auto res = manacher_odd(t + "#");
    return vector<int>(begin(res) + 1, end(res) - 1);
}

class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        string a;
        int n=parent.size();
        vector<vector<int>>g(n);
        vector<int>start(n);
        vector<int>end(n);
        for(int i=1;i<n;i++){
            g[parent[i]].push_back(i);
        }
        for(int i=0;i<n;i++){
            auto &x=g[i];
            sort(x.begin(),x.end());
        }
        function<void(int)>dfs=[&](int u){
            start[u]=a.size();
            for(auto v:g[u])
                dfs(v);
            a.push_back(s[u]);
            end[u]=a.size();
        };
        dfs(0);
        auto mn=manacher(a);
        vector<bool>ans(n);
        for(int u=0;u<n;u++){
            int sz=(end[u]-start[u]);
            int mid=start[u]+sz/2;
            mid*=2;
            if(sz%2==0)
                mid-=1;
            ans[u]=mn[mid]>=sz;
        }
        return ans;
    }
};