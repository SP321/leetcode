class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n=s.size(),m=p.size();
        vector<int>a(26);
        for(auto &c:p)
            a[c-'a']+=1;
        vector<int>b(26);
        int i=0;
        vector<int>ans;
        for(int j=0;j<n;j++){
            b[s[j]-'a']+=1;
            if(j-i+1>m){
                b[s[i]-'a']-=1;
                i+=1;
            }
            if(j>m-2 and equal(a.begin(),a.end(),b.begin()))
                ans.push_back(i);
        }
        return ans;
    }
};