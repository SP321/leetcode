class Solution {
public:
    vector<vector<int>>a;
    int n;
    int m;
    void dfsfill(int i,int j){
        if(i<0||i>=n||j<0||j>=m||!a[i][j])
            return;
        a[i][j]=0;
        dfsfill(i-1,j);
        dfsfill(i+1,j);
        dfsfill(i,j-1);
        dfsfill(i,j+1);
    }

    int numEnclaves(vector<vector<int>>& grid) {
        a=grid;
        n=grid.size();
        m=grid[0].size();
        for(int i=0;i<n;i++){
                dfsfill(i,0);
                dfsfill(i,m-1);
        }
        for(int j=0;j<m;j++){
                dfsfill(0,j);
                dfsfill(n-1,j);
        }
        int ans=0;
        for(int i=1;i<n-1;i++)
            for(int j=1;j<m-1;j++){
                ans+=a[i][j];
                cout<<a[i][j]<<" ";
        }
        return ans;

    }
};