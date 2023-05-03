class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        int m=0;
        int c=0;
        for(int i=0;i<mat.size();i++){
            int cc=0;
            for(int j=0;j<mat[i].size();j++)
                if(mat[i][j]==1)
                    cc++;
            if(cc>c){
                m=i;
                c=cc;
            }
        }
        return {m,c};
    }
};