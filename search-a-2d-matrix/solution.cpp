class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
        int r=matrix.size();
        int c=matrix[0].size();
        int i=0,j=c*r-1;
        while(i<=j){
            int m=i+(j-i)/2;
            int x=matrix[m/c][m%c];
            if(x<target)
                i=m+1;
            else if(x>target)
                j=m-1;
            else
                return 1;
        }
        return 0;
    }
};