class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int>c(k);
        int ct=0;
        for(auto &x:arr){
            x= (k+(x%k))%k;
            int y=(k-x)%k;
            if(c[y]){
                c[y]-=1;
                ct-=1;
            }
            else{
                c[x]+=1;
                ct+=1;
            }
        }
        return ct==0;
    }
};