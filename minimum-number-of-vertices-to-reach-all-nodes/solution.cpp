class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int>p(n);
        for(int i=0;i<n;i++){
            p[i]=i;
        }
        for(auto &edge:edges){
            int u=edge[0];
            int v=edge[1];
            p[v]=u;
        }
        vector<int>ans;

        for(int i=0;i<n;i++)
            if(p[i]==i)
                ans.push_back(i);
        return ans;
    }   
};