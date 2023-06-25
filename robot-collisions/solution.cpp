class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        vector<tuple<int, int, char, int>> robots;
        for(int i = 0; i < positions.size(); i++) {
            robots.push_back({positions[i], healths[i], directions[i], i});
        }
        sort(robots.begin(), robots.end());

        vector<tuple<int, char, int>> stack;
        for(auto& [pos, health, dir, i] : robots) {
            if(dir == 'R') {
                stack.push_back({health, dir, i});
            } else {
                while(!stack.empty() && get<1>(stack.back()) == 'R') {
                    if(get<0>(stack.back()) < health) {
                        stack.pop_back();
                        health--;
                    } else if(get<0>(stack.back()) > health) {
                        get<0>(stack.back())--;
                        health = 0;
                        break;
                    } else {
                        stack.pop_back();
                        health = 0;
                        break;
                    }
                }
                if(health > 0) {
                    stack.push_back({health, dir, i});
                }
            }
        }

        sort(stack.begin(), stack.end(), [](auto& a, auto& b) { return get<2>(a) < get<2>(b); });
        vector<int> result;
        for(auto& [health, dir, i] : stack) {
            result.push_back(health);
        }

        return result;
    }
};