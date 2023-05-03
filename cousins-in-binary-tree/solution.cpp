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
    map<int,int>l;
    map<int,int>p;
    void dfs(TreeNode* i,int x){
        if(i->left){
            int a=i->left->val;
            p[a]=i->val;
            l[a]=x;
            dfs(i->left,x+1);
        }
        if(i->right){
            int a=i->right->val;
            p[a]=i->val;
            l[a]=x;
            dfs(i->right,x+1);
        }
    }
    bool isCousins(TreeNode* root, int x, int y) {
        p[root->val]=-1;
        l[root->val]=-1;
        dfs(root,1);
        return l[x]==l[y] && p[x]!=p[y];
    }
};