class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        set<string> ans;
        for (auto & i : emails) {
            int a = i.find('@');
            string x = i.substr(0, a);
            string y = i.substr(a + 1);
            x.resize(remove(x.begin(), x.end(), '.') - x.begin());
            int b = x.find('+');
            if (b != -1)
                x = x.substr(0, b);
            ans.insert(x + '@' + y);
        }
        return ans.size();
    }
};