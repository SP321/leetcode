class Solution {
public:
    vector<vector<char>>a;
    bool checksudoku(int x,int y,int n){
        bool ans=1;
        vector<int>c(10);
        for(int i=x;i<x+9/n;i++)
            for(int j=y;j<y+n;j++)
                if(a[i][j]!='.')
                    if(c[a[i][j]-'0']++)
                        return 0;
        return 1;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        bool ans=1;
        a=board;
        for(int i=0;i<9;i++)
            ans=ans&&checksudoku(i,0,9);
        for(int i=0;i<9;i++)
            ans=ans&&checksudoku(0,i,1);
        for(int i=0;i<9;i+=3)
            for(int j=0;j<9;j+=3)
                ans=ans&&checksudoku(i,j,3);
        return ans;
    }
};