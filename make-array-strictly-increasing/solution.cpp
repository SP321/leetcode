class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        map<int, int> dp;
        dp[-1] = 0;
        
        sort(arr2.begin(), arr2.end());
        
        for (int a : arr1) {
            map<int, int> dp2;
            for (auto [val, c] : dp) {
                if (a > val) {
                    dp2[a] = min(dp2.count(a) == 0 ? INT_MAX : dp2[a], c);
                }
                auto it = upper_bound(arr2.begin(), arr2.end(), val);
                if (it != arr2.end()) {
                    dp2[*it] = min(dp2.count(*it) == 0 ? INT_MAX : dp2[*it], c + 1);
                }
            }
            if (dp2.empty()) {
                return -1;
            }
            dp = dp2;
        }

        int minValue = INT_MAX;
        for (const auto& [key, value] : dp) {
            if (value < minValue) {
                minValue = value;
            }
        }
        return minValue;
    }
};