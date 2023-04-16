class Solution {
public:
    int addMinimum(string word) {
        int n=word.size();
        int i=0;
        int ans=0;
        for(int j=0;i<n||j%3!=0;j++){
            if(word[i]==('a'+j%3))
                i++;
            else
                ans++;
        }
        return ans;
            
    }
};