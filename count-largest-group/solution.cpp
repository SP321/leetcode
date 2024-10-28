class Solution {
public:
    int countLargestGroup(int n) {
        vector<int>c(37);
        for(int i=1;i<=n;i++){
            int y=0,x=i;
            while(x){
                y+=x%10;
                x/=10;
            }
            c[y]+=1;
        }
        int mx=0;
        for(int &x:c)
            mx=max(mx,x);
        int ans=0;
        for(int &x:c)
            ans+=x==mx;
        return ans;
    }
};