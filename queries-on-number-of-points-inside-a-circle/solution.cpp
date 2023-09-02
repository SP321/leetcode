class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> ans;
        for (const auto& query : queries) {
            int x = query[0], y = query[1], r = query[2];
            int count = 0;
            for (const auto& point : points) {
                int a = point[0], b = point[1];
                if (sqrt((x - a) * (x - a) + (y - b) * (y - b)) <= r) {
                    count++;
                }
            }
            ans.push_back(count);
        }
        return ans;
    }
};