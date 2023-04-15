class Solution {
public:
    vector<int> findColumnWidth(vector<vector<int>>& grid) {
        vector<int>ans;
        for(int i=0;i<grid[0].size();i++){
            int digits=0;
            for(int j=0;j<grid.size();j++){
                int c=0;
                if(grid[j][i]==0){
                    c=1;
                }
                if(grid[j][i]<0){
                    grid[j][i]*=-1;
                    c++;
                }
                while(grid[j][i]>0){
                    grid[j][i]/=10;
                    c++;
                }
                digits=max(c,digits);
            }
            ans.push_back(digits); 
        }
        return ans;
    }
};