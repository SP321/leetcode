class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<vector<int>> x;
        for(int i : nums){
            if(x.size()>0 && x.back().back()==i-1)
                x.back().push_back(i);
            else
                x.push_back({i});
        }
        
        vector<string> ans;
        for(auto i : x){
            if(i.size()==1)
                ans.push_back(to_string(i[0]));
            else
                ans.push_back(to_string(i[0]) + "->" + to_string(i.back()));
        }
        
        return ans;
    }
};

