class Solution {
public:
    int longestPalindrome(string s) {
        vector<int>c(200);
        int ans=0,o=0;
        for(char x:s)
            c[x]+=1;
        for(int &x:c){
            o+=x%2;
            ans+=x-x%2;
        }
        return ans+min(1,o);
    }
};