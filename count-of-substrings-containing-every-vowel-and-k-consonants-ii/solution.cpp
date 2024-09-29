class Solution {
    vector<bool> vowel;
public:
    Solution() {
        vowel.resize(26, false);
        vowel['a' - 'a'] = true;
        vowel['e' - 'a'] = true;
        vowel['i' - 'a'] = true;
        vowel['o' - 'a'] = true;
        vowel['u' - 'a'] = true;
    }

    long long countOfSubstrings(const string& word, int k) {
        int n = word.size();
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            arr[i] = word[i] - 'a';
        }
        return helper(arr, n, k) - helper(arr, n, k - 1);
    }

    long long helper(const vector<int>& arr, int n, int k) {
        long long ans = 0;
        int i = 0;
        vector<int> vcnt(26, 0);
        int v = 0;
        int c = 0;
        for (int j = 0; j < n; ++j) {
            int idx_j = arr[j];
            if (vowel[idx_j]) {
                if (vcnt[idx_j] == 0) {
                    v += 1;
                }
                vcnt[idx_j] += 1;
            } else {
                c += 1;
            }
            while (v == 5 && c > k) {
                int idx_i = arr[i];
                if (vowel[idx_i]) {
                    vcnt[idx_i] -= 1;
                    if (vcnt[idx_i] == 0) {
                        v -= 1;
                    }
                } else {
                    c -= 1;
                }
                i += 1;
            }
            ans += (j - i + 1);
        }
        return ans;
    }
};