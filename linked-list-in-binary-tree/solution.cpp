/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    bool dfs(TreeNode* n1, ListNode* n2, ListNode* head) {
        if (!n2) return true;
        if (!n1) return false;
        bool ans = false;
        if (n1->val == n2->val) {
            ans = dfs(n1->left, n2->next, head) || dfs(n1->right, n2->next, head);
        }
        if (n2 == head) {
            ans = ans || dfs(n1->left, n2, head) || dfs(n1->right, n2, head);
        }
        return ans;
    }

    bool isSubPath(ListNode* head, TreeNode* root) {
        return dfs(root, head, head);
    }
};