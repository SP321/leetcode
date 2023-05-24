class Solution {
 public:
  int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
    constexpr int md = 1e9+7;
    long ans = 0;
    long speedSum = 0;
    vector<pair<int, int>> A;
    priority_queue<int, vector<int>, greater<>> minHeap;

    for (int i = 0; i < n; ++i)
      A.emplace_back(efficiency[i], speed[i]);

    sort(begin(A), end(A), greater<>());

    for (const auto& [e, s] : A) {
      minHeap.push(s);
      speedSum += s;
      if (minHeap.size() > k)
        speedSum -= minHeap.top(), minHeap.pop();
      ans = max(ans, speedSum * e);
    }

    return ans % md;
  }
};