class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        priority_queue<int> h;
        vector<int> order;
        for (int i = 0; i < profits.size(); ++i) {
            order.push_back(i);
        }
        sort(order.begin(), order.end(),[&](int a,int b){return capital[a]<capital[b];});

        int i = 0;
        for (int j = 0; j < k; ++j) {

            while (i < order.size() && capital[order[i]] <= w) {
                h.push(profits[order[i]]);
                ++i;
            }

            if (!h.empty()) {
                w += h.top();
                h.pop();
            }
        }

        return w;
    }
};