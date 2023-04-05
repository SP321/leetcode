class Solution {
public:
    int romanToInt(string s) {
        map<char, int> m = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int ans = 0;
        int prev = 0;
        for (char c : s) {
            int cur = m[c];
            if (cur > prev)
                ans += cur - 2 * prev;
			else
                ans += cur;
            prev = cur;
        }
        return ans;
    }
};