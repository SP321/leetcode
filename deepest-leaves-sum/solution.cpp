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
    map<int,int>d;
    int ma=0;
    void dfs(TreeNode* i,int x){
        ma=max(ma,x);
        d[x]+=i->val;
        if(i->left)
            dfs(i->left,x+1);
        if(i->right)
            dfs(i->right,x+1);
    }
    int deepestLeavesSum(TreeNode* root) {
        dfs(root,0);
        return d[ma];
    }
};