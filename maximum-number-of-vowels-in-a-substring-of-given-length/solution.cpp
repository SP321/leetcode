class Solution {
public:
    int maxVowels(string s, int k) {
        int n=s.size();
        int c=0;
        int i=0;
        int j=0;
        for(;j<k;j++)
            if(string("aeiou").find(s[j])!=-1)
                c++;
        int ans=c;
        for(;j<n;i++,j++){
            if(string("aeiou").find(s[j])!=-1)
                c++;
            if(string("aeiou").find(s[i])!=-1)
                c--;
            ans=max(ans,c);
        }
        return ans;
    }
};