class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> x;
        for (int i = 0; i < arr2.size(); i++) {
            x[arr2[i]] = i;
        }
        sort(arr1.begin(), arr1.end(), [&](int a, int b) {
            a = x.count(a) ? x[a] : 10000 + a;
            b = x.count(b) ? x[b] : 10000 + b;
            return a < b;
        });

        return arr1;
    }
};