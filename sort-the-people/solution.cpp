class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<int>o(names.size());
        for(int i=0;i<names.size();i++)
            o[i]=i;
        sort(o.begin(),o.end(),[&](int x,int y){return heights[x]>heights[y];});
        vector<string>ans;
        for(int &x:o)
            ans.push_back(names[x]);
        return ans;
    }
};