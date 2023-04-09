class Solution
{
public:
    vector<long long> distance(vector<int> &nums)
    {
        vector<long long> ans(nums.size(), 0);
        map<int, vector<int>> index;

        for (int i = 0; i < nums.size(); i++)
            index[nums[i]].push_back(i);

        for (const auto &pair : index)
        {
            const vector<int> &indices = pair.second;
            int n = indices.size();
            vector<long long> prefix(n, 0);
            vector<long long> suffix(n, 0);
            prefix[0] = indices[0];
            suffix[n - 1] = indices[n - 1];
            for (int i = 1; i < n; i++)
            {
                prefix[i] = prefix[i - 1] + indices[i];
                suffix[n - i - 1] = suffix[n - i] + indices[n - i - 1];
            }
            for (int i = 0; i < n; i++)
            {
                long long sum = 0;
                if (i > 0)
                    sum += ((long long)i * indices[i]) - prefix[i - 1];
                if (i < n - 1)
                    sum += suffix[i + 1] - ((long long)(n - i - 1) * indices[i]);
                ans[indices[i]] = sum;
            }
        }
        return ans;
    }
};