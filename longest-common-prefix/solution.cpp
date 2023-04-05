class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n=strs[0].size();
        for(string &s:strs)
             n=min(n,(int)s.size());
        for(int i=0;i<n;i++){
            char ch=strs[0][i];
            bool e=1;
            for(string &s:strs)
                if(s[i]!=ch){
                    e=0;
                    break;
                }
            if(!e)
                return strs[0].substr(0,i);
        }
        return strs[0].substr(0,n);
    }
};