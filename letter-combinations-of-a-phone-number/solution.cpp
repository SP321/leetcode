class Solution {
public:
    vector<string>a;
    vector<string>ans;
    string x;
    int n;
    vector<string> letterCombinations(string digits) {
        char c = 'a';
        x=digits;
        n=digits.size();
        a.resize(10,"");
        for (int i = 2; i <= 9; ++i)
            for (int j = 0; j < ((i == 7 || i == 9) ? 4 : 3); ++j)
                a[i] += c++;
        if(n>0)
            get_combinations(0,"");
        return ans;
    }
    void get_combinations(int i,string prefix){
        if(i==n)
            ans.push_back(prefix);
        else
            for(char x:a[x[i]-'0'])
                get_combinations(i+1,prefix+x);
    }
};