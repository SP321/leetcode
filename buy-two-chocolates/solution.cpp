class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        sort(prices.begin(),prices.end());
        int x=prices[0]+prices[1];
        if(x<=money)
            return money-x;
        return money;
    }
};