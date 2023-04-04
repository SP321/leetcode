class Solution {
public:
    int partitionString(string s) {
        const int n=s.size();
        map<int,int>prev;
        int curstart=0;
        int ans=1;
        for(int i=0;i<n;i++){
            if(prev[s[i]]>curstart){
                ans+=1;
                curstart=i;
            }
            prev[s[i]]=i+1;
        }
        return ans;
    }
};