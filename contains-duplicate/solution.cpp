class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
         map<int,int>c;
         for(int &x:nums){
            if(c[x])
                return 1;
            c[x]++;
         }
         return 0;
        
    }
};