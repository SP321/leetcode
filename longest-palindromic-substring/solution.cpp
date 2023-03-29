class Solution {
public:
    string longestPalindrome(string s) {
        int n=s.size();
        cout<<n<<endl;
        vector<vector<int>>dp(n,vector<int>(n,0));
        int ai=0;
        int len=0;
        for(int i=n-1;i>=0;i--){
            for(int j=i;j<n;j++){
                if(s[i]==s[j])
                    if(j-1<=i+1 || dp[i+1][j-1]==1){
                        dp[i][j]=1;
                        if(j-i+1>len){
                            len=j-i+1;
                            ai=i;
                        }
                    }
            }
        }
        return s.substr(ai,len);

    }
};