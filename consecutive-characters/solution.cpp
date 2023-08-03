class Solution {
public:
    int maxPower(string s) {
        int ans=1,c=1;
        for(int i=1;i<s.size();i++){
            if(s[i]==s[i-1]){
                c+=1;
                ans=max(ans,c);
            }
            else{
                c=1;
            }
        }
        return ans;
    }
};