class Solution {
public:
    vector<int> ans;
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";
        
        int startpos = 0;

        for (int i = num2.size() - 1; i >= 0; --i) {
            int pos = startpos;
            for (int j = num1.size() - 1; j >= 0; --j) {
                int x = num2[i] - '0';
                int y = num1[j] - '0';
                int product = x * y;
                add(pos, product);
                pos++;
            }
            startpos++;
        }
        string result;
        for (int i = ans.size() - 1; i >= 0; --i) {
            result.push_back(ans[i] + '0');
        }
        return result;
    }
    void add(int pos, int value) {
        while (ans.size() <= pos) {
            ans.push_back(0);
        }
        value += ans[pos];
        ans[pos] = value % 10;
        if (value >= 10) {
            add(pos + 1, value / 10);
        }
    }
};