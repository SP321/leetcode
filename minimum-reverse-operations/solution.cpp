class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        vector<bool> lookup(n);
        for (auto& i : banned) 
            lookup[i] = true;
        int d = 0;
        vector<int> ans(n, -1);
        ans[p] = d++;
        vector<set<int>> bst(2);
        for (int i = 0; i < n; ++i) {
            bst[i % 2].emplace(i);
        }
        bst[p % 2].erase(p);
        vector<int> q = {p};
        while (!empty(q)) {
            vector<int> new_q;
            for (auto& p : q) {
                int left = 2 * max(p - (k - 1), 0) + (k - 1) - p;
                int right = 2 * min(p + (k - 1), n - 1) - (k - 1) - p;
                for (auto it = bst[left % 2].lower_bound(left);
                     it != end(bst[left % 2]) && *it <= right;
                     it = bst[left % 2].erase(it)) {
                    if (!lookup[*it]) {
                        ans[*it] = d;
                        new_q.emplace_back(*it);
                    }
                }
            }
            q = move(new_q);
            ++d;
        }
        return ans;
    }
};