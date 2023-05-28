class Solution {

public:
    vector<int> parent;

    unordered_set<int> prime_factors(int n) {
        int i = 2;
        unordered_set<int> factors;
        while (i * i <= n) {
            if (n % i) {
                i += 1;
            }
            else {
                n /= i;
                factors.insert(i);
            }
        }
        if (n > 1) {
            factors.insert(n);
        }
        return factors;
    }

    int find(int i) {
        if (parent[i] != i) {
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }

    void union_find(int i, int j) {
        parent[find(i)] = find(j);
    }
    bool canTraverseAllPairs(vector<int>& nums) {
        int n = nums.size();
        int max_num = *max_element(nums.begin(), nums.end());
        parent.resize(max_num + 1);
        iota(parent.begin(), parent.end(), 0);

        for (int num : nums) {
            unordered_set<int> factors = prime_factors(num);
            for (int factor : factors) {
                union_find(num, factor);
            }
        }

        int group = find(nums[0]);
        for (int i = 1; i < n; i++) {
            if (find(nums[i]) != group || nums[i] == 1) {
                return false;
            }
        }
        return true;
    }
};