class Solution {
public:
    bool isPalindrome(string s) {
        string x="";
        for(char &i:s)
            if(('a'<=i and i<='z') or ('0'<=i and i<='9'))
                x.push_back(i);
            else if('A'<=i and i<='Z')
                x.push_back(i-('A'-'a'));
        int i=0;
        int j=x.size()-1;
        while(i<j)
            if(x[i++]!=x[j--])
                return 0;
        return 1;
    }
};