class Solution {
public:
    bool equalFrequency(string word) {
        for(int i=0;i<word.size();i++){
            vector<int>count(26);
            for(char &a:word)
                count[a-'a']++;
            count[word[i]-'a']--;
            set<int>count2;
            for(int &x:count)
                if(x)
                    count2.insert(x);
            if(count2.size()==1)
                return 1;
        }
        return 0;
    }
};