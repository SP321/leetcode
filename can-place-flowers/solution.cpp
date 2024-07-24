class Solution {
public:
    bool canPlaceFlowers(vector<int>& a, int n) {
        int i=0;
        while(i<a.size()){
            if( (i==0 or a[i-1]==0) and a[i]==0 and (i==a.size()-1 or a[i+1]==0)){
                n-=1;
                i+=1;
            }
            i+=1;
        }
        return n<=0;
    }
};