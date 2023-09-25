class Solution {
int i;
public:
    char findTheDifference(string s, string t) {
        for (i=0;i<s.size();i++){
            t[0] ^= t[i+1];
            t[0] ^= s[i];
        }
        return t[0];
    }
};