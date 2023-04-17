class Solution {
public:
    vector<string>ans;
    void gen(int i,int j,string pre){
        if(j==0){
            ans.push_back(pre);
            return ;
        }
        if(i>0)
            gen(i-1,j,pre+"(");
        if(i<j)
            gen(i,j-1,pre+")");
    }
    vector<string> generateParenthesis(int n) {
        gen(n,n,"");
        return ans;
    }
};