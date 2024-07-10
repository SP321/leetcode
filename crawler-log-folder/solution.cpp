class Solution {
public:
    int minOperations(vector<string>& logs) {
        int c=0;
        for(string &x:logs){
            if (x == "../")
                c=max(0,c-1);
            else if(x=="./")
                ;
            else
                c+=1;
        }
        return c;
    }
};