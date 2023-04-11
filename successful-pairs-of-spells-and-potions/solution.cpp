class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int>spelindex;
        for(int i=0;i<spells.size();i++)
            spelindex.push_back(i);
        sort(spelindex.begin(),spelindex.end(),[&spells](int a,int b){return spells[a]>spells[b];});
        sort(potions.begin(),potions.end());
        int j=0;
        vector<int>ans(spells.size());
        for(int i=0;i<potions.size()&&j<spells.size();i++){
            int z=spells[spelindex[j]];
            if((long long)z*potions[i]>=success){
                ans[spelindex[j]]=potions.size()-i;
                j++;
                i--;
            }
        }
        return ans;
    }
};