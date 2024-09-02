class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> maxHeap(gifts.begin(), gifts.end());

        for (int i = 0; i < k; ++i) {
            int topGift = maxHeap.top();
            maxHeap.pop();
            maxHeap.push(static_cast<int>(sqrt(topGift)));
        }

        long long ans = 0;
        while (!maxHeap.empty()) {
            ans += maxHeap.top();
            maxHeap.pop();
        }

        return ans;
    }
};