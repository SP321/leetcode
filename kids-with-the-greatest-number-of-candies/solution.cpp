class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int ma=0;
        for(int i=0;i<candies.size();i++)
            if(candies[i]>ma)    
                ma=candies[i];
        vector<bool>ans;
        for(int i=0;i<candies.size();i++)
            if(candies[i]+extraCandies>=ma)
                ans.push_back(1);
            else
                ans.push_back(0);
        return ans;
    }
};