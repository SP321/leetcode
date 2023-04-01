class Solution {
public:
    const int mod = 1e9 + 7;
    vector<vector<vector<int>>> dp;
    vector<vector<int>> prefix;   
    int r, c;

    int getSum(int x1, int y1, int x2, int y2){
        // x2 y2 exclusive sum
        return prefix[x2][y2] + prefix[x1][y1] - prefix[x1][y2] - prefix[x2][y1];
    }

    int solve(int i, int j, int k){
        if(dp[i][j][k] != -1)
            return dp[i][j][k];
        if(k == 0)
            return getSum(i, j, r, c) > 0;
        int res = 0;
        // Divide horizontally
        for(int x = i + 1; x < r; x++)
            if(getSum(i, j, x, c) > 0 && getSum(x, j, r, c) > 0)
                res = (res + solve(x, j, k - 1)) % mod;
        // Divide vertically
        for(int y = j + 1; y < c; y++)
            if(getSum(i, j, r, y) > 0 && getSum(i, y, r, c) > 0)
                res = (res + solve(i, y, k - 1)) % mod;
        dp[i][j][k] = res;
        return res;
    }

    int ways(vector<string>& pizza, int k) {
        r = pizza.size();
        c = pizza[0].size();
        prefix.assign(r + 1, vector<int>(c + 1, 0));
        dp.assign(r, vector<vector<int>>(c, vector<int>(k, -1)));
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
                prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + (pizza[i][j] == 'A');
        return solve(0, 0, k - 1);
    }
};