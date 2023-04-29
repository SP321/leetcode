class Solution {
public:
    int n,m;
    void dfs(int x,int y,vector<vector<char>>&a,vector<vector<char>>&b){
        if(x<0 || y<0 ||x>=n ||y>=m || a[x][y]=='X')
            return;
        a[x][y]='X';
        b[x][y]='X';
        dfs(x+1,y,a,b);
        dfs(x-1,y,a,b);
        dfs(x,y+1,a,b);
        dfs(x,y-1,a,b);
    }
    void solve(vector<vector<char>>& board) {
        n=board.size();
        m=board[0].size();
        vector<vector<char>>b(n,vector<char>(m,'X'));
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                b[i][j]=board[i][j];
        for(int i=0;i<n;i++){
            dfs(i,0,b,b);
            dfs(i,m-1,b,b);
        }
        for(int j=0;j<m;j++){
            dfs(0,j,b,b);
            dfs(n-1,j,b,b);
        }
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(b[i][j]=='O')
                    dfs(i,j,b,board);
        return;
    }
};