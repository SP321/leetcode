class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        deque<int> dq;
        for (int i = 0; i < asteroids.size(); i++) {
            if (asteroids[i] > 0 || dq.empty() || dq.back() < 0) {
                dq.push_back(asteroids[i]);
            } else if (dq.back() <= -asteroids[i]) {
                if (dq.back() < -asteroids[i]) {
                    i--;
                }
                dq.pop_back();
            }
        }
        return vector<int>(dq.begin(), dq.end());
    }
};