class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int a = 0, b = -prices[0];
        for(int i : prices) {
            a = std::max(a, b + i - fee);
            b = std::max(b, a - i);
        }
        return a;
    }
};