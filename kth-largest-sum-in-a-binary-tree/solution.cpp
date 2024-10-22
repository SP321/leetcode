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
 auto x=[](){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
 }();

class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        if (!root)
            return -1;

        queue<TreeNode*> q;
        priority_queue<long long, vector<long long>> pq;
        q.push(root);

        while (!q.empty()) {
            long long s = 0;
            int size = q.size();

            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                s += node->val;                
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }

            pq.push(-s);
            if (pq.size() > k) {
                pq.pop();
            }
        }

        if (pq.size() == k) {
            return -pq.top();
        }
        
        return -1;
    }
};