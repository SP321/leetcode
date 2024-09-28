class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        int n=reward1.size();
        vector<int>order(n);
        for(int i=0;i<n;i++)
            order[i]=i;
        sort(order.begin(),order.end(),[&](int i,int j){
            return (reward2[i]-reward1[i]) < (reward2[j]-reward1[j]);
        });
        int ans=0;
        for(int i=0;i<k;i++){
            ans+=reward1[order[i]];
        }
        for(int i=k;i<n;i++){
            ans+=reward2[order[i]];
        }
        return ans;
    }
};