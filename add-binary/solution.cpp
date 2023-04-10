class Solution {
public:
    string addBinary(string a, string b) {
        string ans = "";
        int x = 0;
        int n = a.size() - 1;
        int m = b.size() - 1;
        while (n >= 0 || m >= 0 || x == 1){
            x += ((n >= 0)? a[n] - '0': 0);
            x += ((m >= 0)? b[m] - '0': 0);
            ans = char(x % 2 + '0') + ans;
            x /= 2;
            n--;m--;
        }
        return ans;
    }
};