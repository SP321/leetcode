class Solution {
public:
    int lengthOfLastWord(string s) {
        int ans=0;
        int i=s.size()-1;
        while(s[i]==' ')
            i-=1;
        while(i>=0 and s[i]!=' '){
            i-=1;
            ans+=1;
        }
        return ans;
    }
};