class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        vector<int> x;
        for(int i = 0; i < weights.size() - 1; i++) {
            x.push_back(weights[i] + weights[i + 1]);
        }
        
        sort(x.begin(), x.end());
        
        long long ans = 0;
        for(int i = x.size() - k + 1; i < x.size(); i++) {
            ans += x[i];
        }

        for(int i = 0; i < k - 1; i++) {
            ans -= x[i];
        }
        
        return ans;
    }
};