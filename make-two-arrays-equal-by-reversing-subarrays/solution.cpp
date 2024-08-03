class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        return multiset<int>(target.begin(),target.end())==multiset<int>(arr.begin(),arr.end());
    }
};