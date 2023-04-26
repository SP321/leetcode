class Solution {
public:
    int addDigits(int num) {
        while(num>9){
            int a=0;
            while(num>0){
                a+=num%10;
                num/=10;
            }
            num=a;
        }
        return num;
    }
};