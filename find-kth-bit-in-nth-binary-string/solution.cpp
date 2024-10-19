class Solution {
public:
    char findKthBit(int n, int k) {
        long long sz=1;
        while(n--){
            sz=sz*2+1;
        }
        k-=1;
        int bit=0;
        while(sz){
            long long mid=sz/2;
            if(k>mid){
                bit^=1;
                int diff=k-mid;
                k=mid-diff;
            }
            else if (k==sz/2){
                if(sz>1)
                    bit^=1;
                return '0'+bit;
            }
            sz=sz/2;
        }
        return -1;

    }
};