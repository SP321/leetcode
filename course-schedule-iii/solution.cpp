class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        sort(courses.begin(),courses.end(),[](auto &a,auto &b){
            return a[1]<b[1];
        });
        priority_queue<int>pq;
        int day=0;
        for( auto &x: courses){
            day+=x[0];
            pq.push(x[0]);
            while(day>x[1]){
                day-=pq.top();
                pq.pop();
            }
        }
        return pq.size();
    }
};