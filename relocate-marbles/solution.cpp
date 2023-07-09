class Solution {
public:
    vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom, vector<int>& moveTo) {
        map<int, int> d;
        for (int i : nums) {
            d[i] = 1;
        }

        for (int i = 0; i < moveFrom.size(); i++) {
            if (moveTo[i] != moveFrom[i] && d.count(moveFrom[i]) > 0) {
                d[moveTo[i]] += d[moveFrom[i]];
                d[moveFrom[i]] = 0;
            }
        }

        vector<int> result;
        for (auto& [key, value] : d) {
            if (value > 0) {
                result.push_back(key);
            }
        }

        return result;
    }
};