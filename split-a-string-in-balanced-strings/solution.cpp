class Solution {
public:
    int balancedStringSplit(string s) {
        int ans=0,c=0;
        for(char &x:s){
            if(x=='L')
                c+=1;
            else
                c-=1;
            ans+=c==0;
        }
        return ans;
    }
};