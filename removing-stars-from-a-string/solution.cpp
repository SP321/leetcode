class Solution {
public:
    string removeStars(string s) {
        string ans="";
        for(char &a:s){
            if(a=='*')
                ans.pop_back();
            else
                ans.push_back(a);
        }
        return ans;
    }
};