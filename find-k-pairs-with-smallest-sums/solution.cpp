class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        auto comp = [&nums1, &nums2](pair<int, int>& p1, pair<int, int>& p2) {
            return nums1[p1.first] + nums2[p1.second] > nums1[p2.first] + nums2[p2.second];
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> min_heap(comp);
        
        vector<vector<int>> result;
        if (nums1.empty() || nums2.empty() || k <= 0) return result;

        min_heap.emplace(0, 0);
        while(min_heap.size() > 0 && result.size() < k) {
            pair<int, int> indices = min_heap.top(); min_heap.pop();
            result.push_back({nums1[indices.first], nums2[indices.second]});

            if (indices.second + 1 < nums2.size()) {
                min_heap.emplace(indices.first, indices.second + 1);
            }

            if (indices.second == 0 && indices.first + 1 < nums1.size()) {
                min_heap.emplace(indices.first + 1, 0);
            }
        }

        return result;
    }
};