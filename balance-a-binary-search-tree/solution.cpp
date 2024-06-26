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
    TreeNode* balanceBST(TreeNode* root) {

        vector<TreeNode*> nodes;

        function<void(TreeNode*)> inorder = [&] (TreeNode* node) {
            if (!node) return;
            inorder(node->left);
            nodes.push_back(node);
            inorder(node->right);
        };

        function<TreeNode*(int,int)> helper = [&](int l, int r) {
            if (l == r) return (TreeNode*)nullptr;
            int m = l + (r - l) / 2;
            nodes[m]->left = helper(l, m);
            nodes[m]->right = helper(m + 1, r);
            return nodes[m];
        };
        inorder(root);
        return helper(0, nodes.size());
    }

};