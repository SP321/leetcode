class Solution {
public:
    int sumNumbers(TreeNode* root) {
        function<int(TreeNode*,int)>helper=[&](TreeNode* root, int curSum) {
            if (root == nullptr)
                return 0;
            curSum = curSum * 10 + root->val;
            if (root->left == nullptr && root->right == nullptr)
                return curSum;
            return helper(root->left, curSum) + helper(root->right, curSum);
        };
        return helper(root, 0);
    }
};