class Solution {
public:
    bool checkIfPangram(string sentence) {
        vector<int>a(26);
        for(char &i:sentence)
          a[i-'a']=1;
        for(int &i:a)
          if(!i)
            return 0;
        return 1;
    }
};