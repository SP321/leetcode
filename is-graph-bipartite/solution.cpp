class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        vector<int>s(graph.size());
        for(int i=0;i<graph.size();i++){
            if(s[i]!=0)
                continue;
            s[i] = 1;
            queue<int>q;
            q.push(i);
            while(q.size()){
                int x=q.front();q.pop();
                for(auto &y: graph[x]){
                    if(s[y] == 0){
                        q.push(y);
                        s[y] = -s[x];
                    }
                    else if(s[y] == s[x])
                        return 0;
                }
            }
        }
        return 1;
    }
};