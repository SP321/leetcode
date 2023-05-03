class Solution {
public:
    bool rotateString(string s, string goal) {
        int n=s.size();
        int m=goal.size();
        if(n!=m)
            return 0;
        for(int i=0;i<n;i++){
            bool ans=1;
            for(int k=0;k<n;k++){
                if(s[(k+i)%n]!=goal[k]){
                    ans=0;
                    break;
                }
            }
            if(ans)
                return 1;
        }
        return 0;
    }
};