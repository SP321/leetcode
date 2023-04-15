class Graph {
private:
    int n;
    vector<vector<pair<int, int>>> adjList;

public:
    Graph(int n, vector<vector<int>>& edges) {
        this->n = n;
        adjList.resize(n);
        for (auto& edge : edges) {
            int from = edge[0];
            int to = edge[1];
            int cost = edge[2];
            adjList[from].push_back({to, cost});
        }
    }

    void addEdge(vector<int> edge) {
        int from = edge[0];
        int to = edge[1];
        int cost = edge[2];
        adjList[from].push_back({to, cost});
    }

    int shortestPath(int node1, int node2) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> dist(n, INT_MAX);
        dist[node1] = 0;
        pq.push({0, node1});
        while (!pq.empty()) {
            int currNode = pq.top().second;
            int currDist = pq.top().first;
            pq.pop();
            if (currNode == node2) {
                return currDist;
            }
            if (currDist > dist[currNode]) {
                continue;
            }
            for (auto& neighbor : adjList[currNode]) {
                int neighborNode = neighbor.first;
                int neighborCost = neighbor.second;
                int neighborDist = currDist + neighborCost;
                if (neighborDist < dist[neighborNode]) {
                    dist[neighborNode] = neighborDist;
                    pq.push({neighborDist, neighborNode});
                }
            }
        }
        return -1;
    }
};
