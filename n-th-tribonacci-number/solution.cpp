class Solution {
private:
    vector<int> x;
public:
    Solution() {
        x = {0, 1, 1};
        for (int i = 3; i <= 37; i++) {
            x.push_back(x[i-1] + x[i-2] + x[i-3]);
        }
    }

    int tribonacci(int n) {
        return x[n];
    }
};