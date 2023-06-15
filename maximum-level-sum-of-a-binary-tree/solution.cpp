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
    vector<int> c;
    int maxLevelSum(TreeNode* root) {
        dfs(root, 1);
        int maxIndex = c.size() - 1;
        for (int i = c.size() - 2; i >= 1; --i)
            if (c[i] >= c[maxIndex])
                maxIndex = i;
        return maxIndex;
    }
    void dfs(TreeNode* node, int level) {
        if (!node) return;
        if (level >= c.size())
            c.resize(level + 1);
        c[level] += node->val;
        dfs(node->left, level + 1);
        dfs(node->right, level + 1);
    }
};