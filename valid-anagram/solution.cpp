class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int>c1(26);
        vector<int>c2(26);
        if(s.size()!=t.size())
            return 0;
        for(int i=0;i<s.size();i++){
            c1[s[i]-'a']++;
            c2[t[i]-'a']++;
        }
        
        for(int i=0;i<26;i++){
            if(c1[i]!=c2[i])
                return 0;
        }
        return 1;
    }
};