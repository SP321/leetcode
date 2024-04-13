class Solution {
public:

    int largestRectangleArea(vector < int > & histo) {
        histo.push_back(0);
        stack < int > st;
        int ans = 0;
        int n = histo.size();
        for (int i = 0; i <n; i++) {
            while (!st.empty() &&   histo[i]<histo[st.top()] ) {
                int height = histo[st.top()];
                st.pop();
                int j=st.empty()?-1:st.top();
                int width = i - j - 1;
                ans = max(ans, width * height);
            }
            st.push(i);
        }
        return ans;
    }

    int maximalRectangle(vector<vector<char>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();

        int ans = 0;
        vector<int> height(m, 0);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == '1') height[j]++;
                else height[j] = 0;
            }
            ans = max(largestRectangleArea(height), ans);
        }

        return ans;    
    }
};