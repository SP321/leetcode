class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        const int n=digits.size();
        int c=1;
        for(int j=n-1;j>=0;j--){
            digits[j]+=c;
            if(digits[j]>9){
                c=digits[j]/10;
                digits[j]%=10;
            }else
                c=0;
        }
        if(c!=0)
            digits.insert(digits.begin(),c);
        return digits;
    }
};