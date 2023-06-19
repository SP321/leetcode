/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode*x;
    TreeNode* dfs(TreeNode* i, TreeNode* j){
        TreeNode* y;
        if(i==x)
            return j;
        if(i->left)
            y=dfs(i->left,j->left);
            if(y)
                return y;
        if(i->right)
            y=dfs(i->right,j->right);
            if(y)
                return y;
        return nullptr;
    }
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        x=target;
        return dfs(original,cloned);;
        
    }
};