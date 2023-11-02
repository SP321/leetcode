/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int averageOfSubtree(TreeNode* root) {
        int ans = 0;
        dfs(root, ans);
        return ans;
    }
    
private:
    pair<int, int> dfs(TreeNode* node, int &ans) {
        if (!node) return {0, 0};
        
        auto [lSum, lCount] = dfs(node->left, ans);
        auto [rSum, rCount] = dfs(node->right, ans);
        
        int sum = lSum + rSum + node->val;
        int count = lCount + rCount + 1;
        
        if (sum / count == node->val) ans++;
        
        return {sum, count};
    }
};