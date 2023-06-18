class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int ans=0;
        for(auto&s: sentences)
            ans=max(ans,(int)count(s.begin(),s.end(),' '));
        return ans+1;
    }
};