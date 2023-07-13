class Solution {
public:
    map<int, vector<int>> graph;
    vector<bool> visited;
    vector<bool> stack;

    bool hasCycle(int node) {
        visited[node] = true;
        stack[node] = true;

        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                if (hasCycle(neighbor)) {
                    return true;
                }
            } else if (stack[neighbor]) {
                return true;
            }
        }

        stack[node] = false;
        return false;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        graph.clear();
        visited.assign(numCourses, false);
        stack.assign(numCourses, false);

        for (const auto& prerequisite : prerequisites) {
            graph[prerequisite[0]].push_back(prerequisite[1]);
        }

        for (int i = 0; i < numCourses; ++i) {
            if (!visited[i]) {
                if (hasCycle(i)) {
                    return false;
                }
            }
        }

        return true;
    }
};