class Solution {
public:
    vector<int> resultsArray(vector<vector<int>>& queries, int k) {
        multiset<int>st;
        vector<int>ans;
        for(auto &p:queries){
            st.insert(abs(p[0])+abs(p[1]));
            if(st.size()>k)
                st.erase(prev(st.end()));
            if(st.size()==k)
                ans.push_back(*prev(st.end()));
            else
                ans.push_back(-1);
        }
        return ans;
    }
};