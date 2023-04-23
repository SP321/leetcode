class Solution
{
public:
    vector<int> getSubarrayBeauty(vector<int> &nums, int k, int x)
    {
        vector<int> ans;
        int n = nums.size();
        multiset<int> window;
        for (int i = 0; i < k; i++)
            window.insert(nums[i]);
        auto it = window.begin();
        advance(it, x - 1);
        ans.push_back(min(0, *it));
        window.insert(INT_MAX);
        window.insert(INT_MIN);
        for (int i = 1; i <= n - k; i++)
        {
            int a = nums[i - 1];
            int b = nums[i + k - 1];
            if (a < *it)
            {
                window.erase(window.find(a));
                ++it;
            }
            else if (a == *it)
            {
                ++it;
                window.erase(window.find(a));
            }else{
                window.erase(window.find(a));
            }
            window.insert(b);
            if (b < *it)
            {
                --it;
            }
            ans.push_back(min(0, *it));
        }
        return ans;
    }
};