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
    bool flipEquiv(TreeNode* n1, TreeNode* n2) {
        if (not n1 or not n2)
            return (not n1 and not n2);
        return  (n1->val==n2->val) and \
                (
                    (flipEquiv(n1->left,n2->left) and flipEquiv(n1->right,n2->right) ) or \
                    (flipEquiv(n1->left,n2->right) and flipEquiv(n1->right,n2->left) )
                );
    }
};