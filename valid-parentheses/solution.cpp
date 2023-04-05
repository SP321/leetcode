class Solution {
public:
    bool isValid(string s) {
        stack<char> x;
        x.push('.');
        for(int i=0;i<s.size();i++){
            if(s[i]=='(' || s[i]=='{'|| s[i]=='['){
                x.push(s[i]);
            }else{
                if( (s[i]==')' && x.top()=='(' )||(s[i]=='}' && x.top()=='{' )||(s[i]==']' && x.top()=='[' ))
                    x.pop();
                else
                    return 0;
            }
        }
        if(x.size()==1)
            return 1;
        return 0;
    }
};