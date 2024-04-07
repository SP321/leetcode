class Solution {
public:
    string getSmallestString(string s, int k) {
        for(int i=0;k>0 and i<s.size();i++){
            if(s[i]+k>'z'){
                k-=min('z'-s[i]+1,s[i]-'a');
                s[i]='a';
            }
            else{
                int move=min(s[i]-'a',k);
                k-=move;
                s[i]-=move;
            }
        }
        return s;
    }
};