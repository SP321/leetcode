class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        unordered_map<int, int> c;
        for (int x : bills) {
            c[x]++;
            int change = x - 5;
            for (int y : {10, 5}) {
                int take = min(c[y], change / y);
                c[y] -= take;
                change -= y * take;
            }
            if (change != 0) {
                return false;
            }
        }
        return true;
    }
};