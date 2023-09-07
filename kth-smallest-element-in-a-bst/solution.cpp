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
    int k;
    int kthSmallest(TreeNode* root, int k) {
        this->k=k;
        return inorder(root);
    }

    int inorder(TreeNode* node) {
        if (!node) return -1;

        int left = inorder(node->left);
        
        if (left != -1) return left;

        if (--k == 0) return node->val;

        return inorder(node->right);
    }
};