class Solution {
public:
    int minNumberOperations(vector<int>& a) {
        int ans=0;
        a.push_back(0);
        for(int i=1;i<a.size();i++){
            if(a[i]<a[i-1])
                ans+=a[i-1]-a[i];
        }
        return ans;
    }
};