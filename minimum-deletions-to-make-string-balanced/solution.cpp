class Solution {
public:
    int minimumDeletions(string s) {
        int a=0,b=0;
        for (char c : s)
            if(c=='a')
                a+=1;
        int ans=a;
        for (char c : s) {
            if (c == 'b') {
                b += 1;
            } else {
                a -= 1;
            }
            ans = min(ans, a + b);
        }
        return ans;
    }
};