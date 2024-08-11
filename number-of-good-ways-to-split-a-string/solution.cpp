class Solution {
public:
    int numSplits(string s) {
        int n=s.size();
        vector<int>r(n);
        unordered_set<char>st;
        for(int i=n-1;i>=0;i--){
            st.insert(s[i]);
            r[i]=st.size();
        }
        st.clear();
        int ans=0;
        for(int i=0;i<n-1;i++){
            st.insert(s[i]);
            if(st.size()==r[i+1])
                ans+=1;
        }
        return ans;
    }
};