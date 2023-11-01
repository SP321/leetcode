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
    vector<int> findMode(TreeNode* root) {
        vector<int> result;
        TreeNode* prev = nullptr;
        int count = 1, maxCount = 0;
        
        inOrderTraversal(root, prev, count, maxCount, result);
        
        return result;
    }
    
    void inOrderTraversal(TreeNode* node, TreeNode*& prev, int& count, int& maxCount, vector<int>& result) {
        if (!node) return;
        
        inOrderTraversal(node->left, prev, count, maxCount, result);
        
        if (prev) {
            count = (node->val == prev->val) ? count + 1 : 1;
        }
        if (count > maxCount) {
            maxCount = count;
            result = {node->val};
        } else if (count == maxCount) {
            result.push_back(node->val);
        }
        
        prev = node;
        inOrderTraversal(node->right, prev, count, maxCount, result);
    }
};