class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<int> adj_list[n];   
        vector<int> indegree(n);
        for(int i=0;i<edges.size();++i)
        {
            adj_list[edges[i][0]].push_back(edges[i][1]);
            indegree[edges[i][1]]++;
        }
        queue<int> q;
        for(int i=0;i<n;++i)
        {
            if(indegree[i]==0)
                q.push(i);
        }
        set<int> st[n];
        while(!q.empty())
        {
            
            int cur=q.front(); 
            q.pop();
            
            for(auto it:adj_list[cur])
            {
                st[it].insert(cur); 
                for(auto it2:st[cur])
                    st[it].insert(it2);
                indegree[it]--;
                if(indegree[it]==0)
                q.push(it);
            }
        }
        vector<vector<int>> ans(n,vector<int>());
        
        for(int i=0;i<n;++i)
            ans[i]=vector<int>(st[i].begin(),st[i].end());
        
        
        return ans; 
    }
};