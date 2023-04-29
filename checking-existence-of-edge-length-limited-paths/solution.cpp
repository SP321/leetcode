class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        ios_base::sync_with_stdio(0);
        vector<int>rank(n,0);
        vector<int>parent(n,-1);
        vector<int>o1(edgeList.size());
        vector<int>o2(queries.size());
        for(int i=0;i<edgeList.size();i++)
            o1[i]=i;
        for(int i=0;i<queries.size();i++)
            o2[i]=i;
        sort(o1.begin(),o1.end(),[&edgeList](int x,int y){return edgeList[x][2]<edgeList[y][2];});
        sort(o2.begin(),o2.end(),[&queries](int x,int y){return queries[x][2]<queries[y][2];});
        int j=0;
        int queryindex,edgeindex;
        vector<bool>ans(queries.size());
        for(int i=0;i<queries.size();i++){
            queryindex=o2[i];
            int limit=queries[queryindex][2];
            while(j<edgeList.size()){
                edgeindex=o1[j];
                if(edgeList[edgeindex][2] >= limit)
                    break;
                int a=edgeList[edgeindex][0];
                int b=edgeList[edgeindex][1];
                while(parent[a]!=-1)
                    a=parent[a];
                while(parent[b]!=-1)
                    b=parent[b];
                if (a != b) {
                    if (rank[a] < rank[b]) 
                        parent[a] = b;
                    else if (rank[a] > rank[b])
                        parent[b] = a;
                    else {
                        parent[b] = a;
                        rank[a]++;
                    }
                }
                j++;
            }
            int p=queries[queryindex][0];
            int q=queries[queryindex][1];
            while(parent[p]!=-1)
                p=parent[p];
            while(parent[q]!=-1)
                q=parent[q];
            ans[queryindex]=p==q;
        }
        return ans;
    }
};