class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int>x;
        int j=0;
        for(int i=0;i<pushed.size();i++){
            x.push(pushed[i]);
            while(x.size()&&x.top()==popped[j]){
                x.pop();
                j++;
            }
        }
        return x.size()==0 && j==pushed.size();
    }
};