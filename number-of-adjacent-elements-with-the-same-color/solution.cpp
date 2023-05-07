class Solution {
public:
    vector<int> colorTheArray(int n, vector<vector<int>>& queries) {
        vector<int>a(n);
        int c=0;
        vector<int>ans;
        for(auto &q:queries){
            int i=q[0];
            int x=q[1];
            if(i>0)
                c-= a[i-1]==a[i] && a[i]!=0;
            if(i<n-1)
                c-= a[i+1]==a[i] && a[i]!=0;
            a[i]=x;
            if(i>0)
                c+=a[i-1]==a[i];
            if(i<n-1)
                c+=a[i+1]==a[i];
            ans.push_back(c);
        }
        return ans;
    }
};