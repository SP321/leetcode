class Solution {
public:
    long long triangle(long long n) {
        if(n<=0)
            return 0;
        return (n * (n + 1)) / 2;
    }
    int numberOfSubstrings(string s) {
        int n = s.length();
        vector<int> z = {-1};
        for (long long i = 0; i < n; ++i) {
            if (s[i] == '0') {
                z.push_back(i);
            }
        }
        z.push_back(n);

        long long ans = 0;
        for (int i = 1; i < z.size(); ++i) {
            ans += triangle(z[i] - z[i - 1] - 1);
        }
        int max_zeros =(int)(sqrt(n - (z.size() - 2))) + 1;
        for (int zero_c = 1; zero_c < max_zeros; ++zero_c) {
            for (int i = 1; i < int(z.size()) - zero_c; ++i) {
                int j = i + zero_c - 1;
                int l = z[i] - z[i - 1];
                int r = z[j + 1] - z[j];
                int min_ones = zero_c * zero_c;
                int window_sz = z[j] - z[i] + 1;
                int have_ones = window_sz - zero_c;
                int take = min_ones - have_ones;

                if (take < l + r) {
                    ans += l * r;
                    ans -= triangle(take);
                    ans += triangle(take - l);
                    ans += triangle(take - r);
                }
            }
        }
        return ans;
    }
};