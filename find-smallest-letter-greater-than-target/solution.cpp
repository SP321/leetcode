class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        char ans=CHAR_MAX;
        for(auto&c:letters)
            if(c>target && c<ans)
                ans=c;
        if(ans!=CHAR_MAX)
            return ans;
        return letters[0];
    }
};
