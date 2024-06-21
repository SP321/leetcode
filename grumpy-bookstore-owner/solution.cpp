class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int total = 0;
        int n = customers.size();
        int i = 0;
        int cur = 0;
        int ans = 0;

        for (int j = 0; j < n; ++j) {
            if (grumpy[j]) {
                cur += customers[j];
            } else {
                total += customers[j];
            }

            if (j - i + 1 > minutes) {
                if (grumpy[i]) {
                    cur -= customers[i];
                }
                ++i;
            }

            ans = max(ans, cur);
        }

        return ans + total;
    }
};