const int MAX = int(1e6)+1;
vector<int> sieve(MAX, INT_MAX);

auto x = []() {
    for (int i = MAX - 1; i >= 2; --i) {
        for (int j = i + i; j < MAX; j += i) {
            sieve[j] = i;
        }
    }
    return 0;
}();

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int limit = nums.back();
        int ans = 0;

        while (!nums.empty()) {
            int cur = nums.back();
            nums.pop_back();

            if (cur > limit) {
                cur = sieve[cur];
                if (cur > limit) {
                    return -1;
                }
                ans++;
            }
            limit = cur;
        }

        return ans;
    }
};
