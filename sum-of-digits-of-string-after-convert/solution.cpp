class Solution {
public:
    int getLucky(string s, int k) {
        string ans = "";
        for (char x : s) {
            ans += to_string(x - 'a' + 1);
        }
        
        while (k--) {
            int temp = 0;
            for (char x : ans) {
                temp += x - '0';
            }
            ans = to_string(temp);
        }
        return stoi(ans);
    }
};