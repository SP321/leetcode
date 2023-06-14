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
    int getMinimumDifference(TreeNode* root) {
        dfs(root);
        return ans;
    }
    int ans=1e6;
    int prev=-1e6;
    void dfs(TreeNode* i){
        if(i->left)
            dfs(i->left);
        const int cur=i->val;
        ans=min(ans,abs(cur-prev));
        prev=cur;
        if(i->right)
            dfs(i->right);
    }
};