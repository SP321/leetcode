class Solution {
public:
    string merge(string x, string y) {
        if (x.find(y) != string::npos)
            return x;
        for (int j = min(y.length(), x.length()); j > 0; --j) {
            if (y.substr(0, j) == x.substr(x.length() - j))
                return x + y.substr(j);
        }
        return x+y;
    }
    string minimumString(string a, string b, string c) {
        vector<string> s = {a, b, c};
        vector<vector<int>> orders = {{0,1,2}, {0,2,1}, {1,0,2}, {1,2,0}, {2,0,1}, {2,1,0}};

        string ans = a + b + c;

        for(auto& order : orders) {
            string merged = merge(s[order[0]], s[order[1]]);
            merged = merge(merged, s[order[2]]);
            if (merged.length() < ans.length() || (merged.length() == ans.length() && merged < ans)) {
                ans = merged;
            }
        }

        return ans;
    }
};