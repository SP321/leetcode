class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int n = coordinates.size();
        int x1 = coordinates[0][0];
        int y1 = coordinates[0][1];
        int x2 = coordinates[1][0];
        int y2 = coordinates[1][1];
        float m;
        if (x2 - x1 == 0)
            m = INFINITY;
        else
            m = (float)(y2 - y1) / (x2 - x1);
        for (int i = 1; i < n - 1; ++i) {
            x1 = coordinates[i][0];
            y1 = coordinates[i][1];
            x2 = coordinates[i+1][0];
            y2 = coordinates[i+1][1];
            float m2;
            if (x2 - x1 == 0)
                m2 = INFINITY;
            else
                m2 = (float)(y2 - y1) / (x2 - x1);
            if (m != m2)
                return false;
        }
        return true;
    }
};