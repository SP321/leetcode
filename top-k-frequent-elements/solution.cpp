class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int>c;
        for(int &x:nums)
            c[x]++;
        vector<int>c1;
        vector<int>c2;
        vector<int>a;
        int l=0;
        for(auto &p:c){
            c2.push_back(p.second);
            c1.push_back(p.first);
            l++;
        }
        for(int i=0;i<l;i++)
            a.push_back(i);
        sort(a.begin(),a.end(),[&c2](int a,int b){return c2[a]>c2[b];});
        vector<int>ans;
        int n=nums.size();
        for(int i=0;i<k;i++)
            ans.push_back(c1[a[i]]);
        return ans;
    }
};