class Solution {
public:
    int minimumSum(int num) {
        vector<int> d;
        while(num > 0) {
            d.push_back(num % 10);
            num /= 10;
        }
        sort(d.begin(),d.end());
        return (10*d[0] + d[2]) + (10*d[1] + d[3]);
    }
};