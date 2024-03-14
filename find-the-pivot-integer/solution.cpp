class Solution {
public:
    int pivotInteger(int n) {
        float ans=sqrt((n*n+n)/2);
        return ans==floor(ans)?(int)ans:-1;
    }
};