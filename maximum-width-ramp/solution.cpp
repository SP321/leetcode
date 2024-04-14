class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        stack<int>st;
        int ans=0;
        for(int i=0;i<nums.size();i++){
            if(st.empty() or nums[st.top()] > nums[i])
                st.push(i);
        }
        for(int i=nums.size()-1;i>0;i--){
            while( not st.empty() and nums[st.top()] <= nums[i]){
                ans = max(ans, i - st.top());
                st.pop();
            }
        }
        return ans;
    }
};