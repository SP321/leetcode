class Solution {
public:
    int captureForts(vector<int>& forts) {
        int ans = 0; 
        for (int i = 0, ii = 0; i < forts.size(); ++i) 
            if (forts[i]) {
                if (forts[ii] == -forts[i])
                    ans = max(ans, i-ii-1); 
                ii = i; 
            }
        return ans; 
    }
};