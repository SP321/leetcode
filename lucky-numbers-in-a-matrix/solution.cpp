class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        unordered_map<int,int>c;
        for(int i=0;i<matrix.size();i++){
            int mi=1e6;
            for(int j=0;j<matrix[0].size();j++){
                mi=min(mi,matrix[i][j]);
            }
            c[mi]+=1;
        }
        vector<int>ans;
        for(int j=0;j<matrix[0].size();j++){
            int mx=-1;
            for(int i=0;i<matrix.size();i++){
                mx=max(mx,matrix[i][j]);
            }
            if(c.count(mx))
                ans.push_back(mx);
        }
        return ans;
    }
};