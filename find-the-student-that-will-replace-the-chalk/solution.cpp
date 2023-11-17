class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long long s=0;
        for(auto &i:chalk)
            s+=i;
        k%=s;
        int n=chalk.size();
        for(int i=0;i<n;i++){
            if(k<chalk[i])
                return i;
            k-=chalk[i];
        }
        return 69;
    }
};