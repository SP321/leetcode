class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead(deadends.begin(), deadends.end());
        if (dead.count("0000")) return -1;
        auto get_neighbors = [](const string& x) -> vector<string> {
            vector<string> ans;
            for (int i = 0; i < 4; ++i) {
                char cur = x[i];
                string temp = x;
                temp[i] = (cur - '0' + 1) % 10 + '0';
                ans.push_back(temp);
                temp[i] = (cur - '0' + 9) % 10 + '0';
                ans.push_back(temp);
            }
            return ans;
        };
        
        queue<string> q;
        q.push("0000");
        int ans = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                string x = q.front();
                q.pop();
                if (x == target)
                    return ans;
                for (const string& nei : get_neighbors(x)) {
                    if (!dead.count(nei)) {
                        dead.insert(nei);
                        q.push(nei);
                    }
                }
            }
            ++ans;
        }
        return -1;
    }
};