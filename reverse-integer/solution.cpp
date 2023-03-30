class Solution {
public:
    int reverse(int x) {
        int sign=x<0?-1:1;
        uint rev=0;
        uint y=abs(x);
        while(y>0){
            uint overflow=1<<31;
            uint rem=y%10;
            if(overflow/10<rev || rev==overflow/10 &&  rem>10)
                return 0;
            rev=rev*10+rem;
            y/=10;
        }
        return (int)sign*rev;
    }
};