class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(size(s)==0)
            return 0;
        int ans=1;
        map<char,int>prev;
        int m=0;
        for(int i=0;i<s.size();i+=1){
            if(prev[s[i]])
                m=max(m,prev[s[i]]);
            prev[s[i]]=i+1;
            ans=max(ans,i-m+1);
        }
        return ans;
    }
};