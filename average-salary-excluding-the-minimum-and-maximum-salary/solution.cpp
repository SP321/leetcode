class Solution {
public:
    double average(vector<int>& salary) {
        int n=salary.size();
        double s=0;
        int mi=INT_MAX;
        int ma=0;
        for(int i=0;i<n;i++){
            s+=salary[i];
            mi=min(mi,salary[i]);
            ma=max(ma,salary[i]);
        }
        return (s-mi-ma)/(n-2);
    }
};