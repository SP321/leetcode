class Solution {
public:
    long long minimumCost(string s) {
        long long ans = 0;
        int n = s.size();
        if (n == 1)
            return 0;

        ans += solve(s, 0, n / 2, 1);
        ans += solve(s, n - 1, n / 2 - 1, -1);

        if (s[n / 2 - 1] != s[n / 2])
            ans += n / 2;

        return ans;
    }

private:
    long long solve(string s, int start, int end, int increment) {
        long long a = 0;
        for (int i = start; i != end; i += increment) {
            if (i != end - increment && s[i] != s[i + increment]) {
                a += abs(i - start) + 1;
            }
        }
        return a;
    }
};