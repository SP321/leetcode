class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n=strs.size();
        map<string,vector<string>>ans;
        for(int i=0;i<n;i++){
            vector<int>c(26);
            for(int j=0;j<strs[i].size();j++)
                c[strs[i][j]-'a']++;
            string x="";
            for(int j=0;j<26;j++)
                x.push_back((char)c[j]+'a');
            ans[x].push_back(strs[i]);
        }
        vector<vector<string>>ans2;
        for(auto &pair:ans)
            ans2.push_back(pair.second);
        return ans2;
    }
};