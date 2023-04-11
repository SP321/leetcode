class Solution {
public:
    int myAtoi(string s) {
        if(!s.size())
            return 0;
        int i=0;
        int ans=0;
        while(s[i]==' ')
            i++;
        int sign= s[i]=='-'?-1:1;
        if(s[i]=='-'||s[i]=='+')
            i++;
        while(i<s.size()){
            if(s[i]>='0' && s[i]<='9'){
                if((ans>(INT_MAX-1)/10 && sign==1)||(ans>INT_MAX/10 && sign==-1))
                    return sign>0?INT_MAX:-1*INT_MAX-1;
                ans*=10;
                if((ans>INT_MAX-1-s[i]+'0' && sign==1)||(ans>INT_MAX-s[i]+'0' && sign==-1))
                    return sign>0?INT_MAX:-1*INT_MAX-1;
                ans+=s[i]-'0';
            }else
                break;
            i++;
        }
        return sign*ans;
        
    }
};