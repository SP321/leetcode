class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows==1)
            return s;
        string ans="";
        for(int i=0;i<numRows;i++){
            for(int j=i;j<s.size();){
                ans+=s[j];
                if(((j)/(numRows-1))%2==0)
                    j+=(numRows-i)*2-2;
                else
                    j+=(i+1)*2-2;
            }
        }
        return ans;
    }
};