class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        priority_queue<int>pq;
        int ans=0;
        sort(intervals.begin(),intervals.end());
        for(auto &x:intervals){
            while(not pq.empty() and -pq.top()<x[0])
                pq.pop();
            pq.push(-x[1]);
            ans=max(ans,(int)pq.size());
        }
        return ans;
    }
};
auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();