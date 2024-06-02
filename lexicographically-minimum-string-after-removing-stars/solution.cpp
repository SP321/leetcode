class Solution {
public:
    string clearStars(const string& s) {
        priority_queue<pair<char, int>> h;
        unordered_set<int>dels;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != '*') {
                h.push({-s[i], i});
            } else{
                auto p = h.top();h.pop();
                dels.insert(p.second);
            }
        }

        string ans;
        for (int i = 0; i < s.size(); ++i) {
            if ( s[i]!='*' and dels.find(i)==dels.end()){
                ans += s[i];
            }
        }
        return ans;
    }
};