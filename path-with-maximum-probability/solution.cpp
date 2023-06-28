class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        vector<vector<pair<int, double>>> graph(n);
        for (int i = 0; i < edges.size(); i++) {
            graph[edges[i][0]].push_back({edges[i][1], succProb[i]});
            graph[edges[i][1]].push_back({edges[i][0], succProb[i]});
        }

        vector<double> prob(n, 0);
        prob[start] = 1.0;

        priority_queue<pair<double, int>> pq;
        pq.push({1.0, start});

        while (!pq.empty()) {
            auto [pr, node] = pq.top(); pq.pop();
            if (pr < prob[node]) continue;
            for (auto &[next, edgeProb] : graph[node]) {
                if (prob[node] * edgeProb > prob[next]) {
                    prob[next] = prob[node] * edgeProb;
                    pq.push({prob[next], next});
                }
            }
        }
        return prob[end];
    }
};