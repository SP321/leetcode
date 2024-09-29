class Solution {
public:
    long long countOfSubstrings(const string& word, int k) {
        n = word.length();
        this->word = word;
        long long ans1 = count_substrings(k);
        long long ans2 = count_substrings(k - 1);
        return ans1 - ans2;
    }

private:
    int n;
    string word;

    bool check(const unordered_map<char, int>& c, int kk) {
        for (char x : {'a', 'e', 'i', 'o', 'u'}) {
            if (c.find(x) == c.end() || c.at(x) < 1)
                return false;
        }
        int ct = 0;
        for (const auto& pair : c) {
            char x = pair.first;
            if (pair.second > 0 && x != 'a' && x != 'e' && x != 'i' && x != 'o' && x != 'u') {
                ct += pair.second;
            }
        }
        return ct > kk;
    }

    long long  count_substrings(int max_consonants) {
        long long ans = 0;
        int i = 0;
        unordered_map<char, int> ct;
        for (int j = 0; j < n; ++j) {
            ct[word[j]] += 1;
            while (i <= j && check(ct, max_consonants)) {
                ct[word[i]] -= 1;
                if (ct[word[i]] == 0)
                    ct.erase(word[i]);
                i += 1;
            }
            ans += (j - i + 1);
        }
        return ans;
    }
};