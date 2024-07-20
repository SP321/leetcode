class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        int n=rowSum.size();
        int m=colSum.size();
        vector<vector<int>>a(n,vector<int>(m));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                a[i][j]=min(rowSum[i],colSum[j]);
                rowSum[i]-=a[i][j];
                colSum[j]-=a[i][j];
            }
        }
        return a;
    }
};