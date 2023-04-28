class Solution {
public:
    bool similar(string a,string b){
        int c=0;
        for(int i=0;i<a.size();i++){
            if(c>2)
                return 0;
            if(a[i]!=b[i])
                c++;
        }

        return (c==0 || c==2);
    }
    int numSimilarGroups(vector<string>& strs) {
        int n=strs.size();
        vector<int>p(n,-1);
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(similar(strs[i],strs[j])){
                    int x=i;
                    int y=j;
                    while(p[x]!=-1)
                        x=p[x];
                    while(p[y]!=-1)
                        y=p[y];
                    if(x!=y)
                        p[y]=x;
                }
            }
        }
        int ans=0;
        for(int i=0;i<n;i++)
            cout<<p[i]<<" ";
        for(int i=0;i<n;i++)
            if(p[i]==-1)
                ans++;
        return ans;
    }
};