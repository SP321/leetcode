class SeatManager {
public:
    priority_queue<int, vector<int>, greater<int>> x;
    int pos=0;

    SeatManager(int n) {
    }

    int reserve() {
        if (x.empty()) {
            pos+=1;
            return pos;
        } else {
            int a = x.top();
            x.pop();
            return a;
        }
    }

    void unreserve(int seatNumber) {
        x.push(seatNumber);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */