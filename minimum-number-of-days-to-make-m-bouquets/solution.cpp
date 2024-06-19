class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        auto isValid = [&](int x) {
            int total = 0;
            int currcount = 0;
            for (int b : bloomDay) {
                if (x >= b) {
                    currcount += 1;
                } else {
                    total += currcount / k;
                    if (total >= m) {
                        return true;
                    }
                    currcount = 0;
                }
            }
            total += currcount / k;
            return total >= m;
        };

        if (1ll* m * k > bloomDay.size()) {
            return -1;
        }

        int left = *min_element(bloomDay.begin(), bloomDay.end());
        int right = *max_element(bloomDay.begin(), bloomDay.end());
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isValid(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};