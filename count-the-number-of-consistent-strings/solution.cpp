class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        bitset<26> s=0;
        for(char c: allowed)
            s[c-'a']=1;
        int ans=words.size();
        for(string& w: words){
            for(char c: w){
                if (s[c-'a']==0){
                    ans-=1;
                    break;
                }
            }
        }
        return ans;
    }
};