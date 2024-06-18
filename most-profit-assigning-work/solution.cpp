class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int n=profit.size();
        sort(worker.begin(),worker.end());
        vector<int>order(n);
        for(int i=0;i<n;i++)
            order[i]=i;
        sort(order.begin(),order.end(),[&](int a,int b){return difficulty[a]<difficulty[b];});
        int i=0,cur=0,ans=0;
        for(int &x:worker){
            while(i<n and difficulty[order[i]]<=x){
                cur=max(cur,profit[order[i]]);
                i++;
            }
            ans+=cur;
        }
        return ans;
    }
};