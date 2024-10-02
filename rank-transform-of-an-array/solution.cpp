class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        set<int>st;
        for(auto &x:arr)
            st.insert(x);
        unordered_map<int,int>mp;
        int rank=1;
        for(auto &x:st){
            mp[x]=rank++;
        }
        for(auto &x:arr)
            x=mp[x];
        return arr;
    }
};