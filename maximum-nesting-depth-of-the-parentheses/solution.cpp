class Solution {
public:
    int maxDepth(string s) {
        int ans=0;
        int ct=0;
        for(char &x:s){
            if(x=='('){
                ct+=1;
                ans=max(ans,ct);
            }
            else if(x==')'){
                ct-=1;
            }
        }
        return ans;
    }
};