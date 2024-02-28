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
    void findBottomLeftValueDFS(TreeNode* node, int depth, int& maxDepth, int& leftmostValue) {
        if (node == nullptr) return;
        // If this is the first node of its level
        if (depth > maxDepth) {
            maxDepth = depth;
            leftmostValue = node->val;
        }
        // Traverse left subtree first to ensure leftmost node is encountered first at each level
        findBottomLeftValueDFS(node->left, depth + 1, maxDepth, leftmostValue);
        findBottomLeftValueDFS(node->right, depth + 1, maxDepth, leftmostValue);
    }
    
    int findBottomLeftValue(TreeNode* root) {
        int maxDepth = -1, leftmostValue = 0;
        findBottomLeftValueDFS(root, 0, maxDepth, leftmostValue);
        return leftmostValue;
    }
};