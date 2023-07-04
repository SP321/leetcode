class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int,int>x;
        for(int &i:nums)
            x[i]++;
        for(int &i:nums)
            if(x[i]==1)
                return i;
        return 69;
    }
};