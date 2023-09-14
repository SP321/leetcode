class Solution {
private:
    unordered_map<string, vector<string>> graph;
    vector<string> itinerary;

    void dfs(const string& airport) {
        while (!graph[airport].empty()) {
            string nextAirport = graph[airport].back();
            graph[airport].pop_back();
            dfs(nextAirport);
        }
        itinerary.push_back(airport);
    }

public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        graph.clear();
        itinerary.clear();

        for (auto& ticket : tickets) {
            graph[ticket[0]].push_back(ticket[1]);
        }

        for (auto& item : graph) {
            sort(item.second.begin(), item.second.end(), greater<string>());
        }

        dfs("JFK");
        reverse(itinerary.begin(), itinerary.end());

        return itinerary;
    }
};