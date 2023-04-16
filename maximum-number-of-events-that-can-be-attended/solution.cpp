class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        int n = events.size();
        sort(events.begin(), events.end());
        priority_queue<int, vector<int>, greater<int>> pq;
        int ans = 0, i = 0;
        for (int curday = 1; curday <= 100000; curday++) {
            while (i < n && events[i][0] == curday) {
                pq.push(events[i][1]);
                i++;
            }
            while (!pq.empty() && pq.top() < curday) {
                pq.pop();
            }
            if (!pq.empty()) {
                ans++;
                pq.pop();
            }
        }
        return ans;
    }
};