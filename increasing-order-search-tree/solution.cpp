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
    TreeNode* head;
    TreeNode* tail;
    TreeNode* increasingBST(TreeNode* root) {
        traverse(root);
        return head;
    }
    void traverse(TreeNode* root){
        if(!root)
            return;
        traverse(root->left);
        TreeNode* newnode=new TreeNode(root->val);
        if(head==nullptr)
            head=newnode;
        else
            tail->right=newnode;
        tail=newnode;
        traverse(root->right);
    }
};