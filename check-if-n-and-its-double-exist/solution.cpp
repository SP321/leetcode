class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int>st;
        for(int &x:arr){
            if ( (x%2==0 and st.find(x/2)!=st.end()) or st.find(x*2)!=st.end()){
                return true;
            }
            st.insert(x);
        }
        return false;
    }
};