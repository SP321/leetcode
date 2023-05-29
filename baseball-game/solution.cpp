class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> x;
        int sum = 0;
        for (const string& op : operations) {
            if (op == "C") {
                sum -= x.back();
                x.pop_back();
            } else if (op == "D") {
                x.push_back(x.back() * 2);
                sum += x.back();
            } else if (op == "+") {
                x.push_back(x.back() + x[x.size() - 2]);
                sum += x.back();
            } else {
                x.push_back(stoi(op));
                sum += x.back();
            }
        }
        return sum;
    }
};