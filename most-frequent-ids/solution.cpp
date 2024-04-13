class Solution {
public:
    vector<long long> mostFrequentIDs(vector<int>& nums, vector<int>& freq) {
        unordered_map<int,long long>c;
        multiset<long long>x;
        vector<long long>ans;
        for(int i=0;i<nums.size();i++){
            auto itr = x.find(c[nums[i]]);
            if(itr!=x.end()){
                x.erase(itr);
            }
            c[nums[i]]+=freq[i];
            x.insert(c[nums[i]]);
            ans.push_back(*prev(x.end()));
        }
        return ans;
    }
};