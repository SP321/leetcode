class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int>x;
        for(string &y:tokens){
            if(y== "+"){
                    int a=x.top();x.pop();
                    int b=x.top();x.pop();
                    x.push(a+b);
            }
            else if(y== "-"){
                    int a=x.top();x.pop();
                    int b=x.top();x.pop();
                    x.push(b-a);
            }
            else if(y== "*"){
                    int a=x.top();x.pop();
                    int b=x.top();x.pop();
                    x.push(a*b);
            }
            else if(y== "/"){
                    int a=x.top();x.pop();
                    int b=x.top();x.pop();
                    x.push(b/a);
            }
            else{
                int val=0;
                int sign=1;
                for(char &a:y){
                    if(a=='-')
                        sign=-1;
                    else 
                        val=val*10+a-'0';
                }
                x.push(val*sign);
            }
            cout<<x.top()<<endl;
        }
        return x.top();
    }
};