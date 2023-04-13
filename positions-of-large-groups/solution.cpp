class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        int j=0;
        vector<vector<int>>ans;
        for(int i=0;i<s.size();i++){
            if(i==s.size()-1 || s[i+1]!=s[j]){
                if(i-j+1>=3)
                    ans.push_back({j,i});
                j=i+1;
            }
        }
        return ans;
    }
};