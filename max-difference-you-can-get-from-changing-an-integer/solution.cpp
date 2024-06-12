class Solution {
public:
    int maxDiff(int num) {
 string s = to_string(num);
        string x = s;
        string y = s;
        int n = s.size();

        for (int i = 0; i < n; ++i) {
            if (s[i] > '1') {
                char newChar = (i == 0 ? '1' : '0');
                for (int j = i; j < n; j++) {
                    if (s[j] == s[i]) {
                        x[j] = newChar;
                    }
                }
                break;
            }
        }

        for (int i = 0; i < n; ++i) {
            if (s[i] != '9') {
                for (int j = i; j < n; j++) {
                    if (s[j] == s[i]) {
                        y[j] = '9';
                    }
                }
                break;
            }
        }

        return stoi(y) - stoi(x);
    }
};