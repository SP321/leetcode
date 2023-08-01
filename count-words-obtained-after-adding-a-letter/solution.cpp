class Solution {
public:
    int gethash(string s) {
        int bit_mask = 0;
        for (char c : s) {
            bit_mask |= (1 << (c - 'a'));
        }
        return bit_mask;
    }

    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        map<int,int>d;
        for (string& word : startWords)
            d[gethash(word)]=1;

        int ans = 0;
        for (string& word : targetWords) {
            int bit_mask=gethash(word);
            for (int i = 0; i < 26; ++i)
                if (bit_mask&(1 << i) && d[bit_mask - (1 << i)]){
                    ans+=1;
                    break;
                }
        }
        return ans;
    }
};