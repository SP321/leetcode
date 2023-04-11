class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        vector<int>count(limit+1,0);
        int ans=0;
        for(int &x:people)
            count[x]++;
        int pairs,j;
        for(int i=1;i<count.size();i++){
            j=limit-i;
            while(count[i]&&j>i){
                pairs=min(count[i],count[j]);
                ans+=pairs;
                count[j]-=pairs;
                count[i]-=pairs;
                j--;
            }
            if(i*2<=limit)
                ans+=count[i]/2+count[i]%2;
            else
                ans+=count[i];
        }
        return ans;
    }
};