class Solution {
public:
    string defangIPaddr(string address) {
        string ans="";
        for(char &a:address)
            if(a=='.')
                ans+="[.]";
            else
                ans+=a;
        return ans;
    }
};