class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<int> a(n);
        for (const auto& x : roads) {
            a[x[0]]++;
            a[x[1]]++;
        }
        sort(a.begin(), a.end(), greater<int>() );
        long long ans = 0;

        for (int &x  : a) {
            ans += 1ll* x * n;
            n--;
        }

        return ans;
    }
};