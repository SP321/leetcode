class Solution {
private:
    int countBits(int number) {
        int count = 0;
        while (number) {
            count += number & 1;
            number >>= 1;
        }
        return count;
    }
    vector<int> generateCombination(int number, int n) {
        vector<int> combination;
        for (int i = 0; i < n; i++) {
            if ((number >> i) & 1) {
                combination.push_back(i + 1);
            }
        }
        return combination;
    }

public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> combinations;
        int number = (1 << k) - 1;
        while (number < (1 << n)) {
            combinations.push_back(generateCombination(number, n));
            int t = number & -number;
            int r = number + t;
            number = (((r^number) >> 2) / t) | r;
        }
        return combinations;
    }
};