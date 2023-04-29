class Solution {
public:
    int n,m;
    vector<vector<char>>g;
    void dfs(int x,int y){
        if(x<0 || y<0 || x>=n || y>=m || g[x][y]=='0')
            return;
        g[x][y]='0';
        dfs(x+1,y);
        dfs(x-1,y);
        dfs(x,y+1);
        dfs(x,y-1);
    }
    int numIslands(vector<vector<char>>& grid) {
        g=grid;
        n=g.size();
        m=g[0].size();
        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(g[i][j]=='1'){
                    ans++;
                    dfs(i,j);
                }
            }
        }
        return ans;
    }
};