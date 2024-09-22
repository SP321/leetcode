class Solution {
public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, greater<tuple<long long, int, int>>> pq;
        for (int x : workerTimes) {
            pq.push({x, x, 1});
        }
        long long ans = 0;
        for (int i = 0; i < mountainHeight; ++i) {
            auto [t, x, k] = pq.top();pq.pop();
            ans = t;
            pq.push({t + 1ll * x * (k + 1), x, k + 1});
        }
        return ans;
    }
};