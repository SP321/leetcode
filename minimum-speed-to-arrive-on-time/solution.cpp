class Solution {
public:
    vector<int> dist;
    double hour;
    double check(int speed) {
        double total_time = 0;
        for (int i = 0; i < dist.size() - 1; ++i) {
            total_time += (dist[i] + speed - 1) / speed;
        }
        total_time += (double)dist.back() / speed;
        return total_time;
    }

    int minSpeedOnTime(vector<int>& dist, double hour) {
        this->dist=dist;
        this->hour=hour;
        int left = 1;
        int right = int(1e7);

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (check(mid) > hour) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return check(left) <= hour ? left : -1;
    }
};