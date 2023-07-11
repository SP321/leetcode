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
    map<TreeNode*, vector<TreeNode*>> graph;
    vector<int> ans;
    set<TreeNode*> seen;

    void dfs(TreeNode* node) {
        if (node->left) {
            dfs(node->left);
            graph[node].push_back(node->left);
            graph[node->left].push_back(node);
        }
        if (node->right) {
            dfs(node->right);
            graph[node].push_back(node->right);
            graph[node->right].push_back(node);
        }
    }

    void dfs2(TreeNode* node, int k) {
        seen.insert(node);
        if (k == 0) {
            ans.push_back(node->val);
            return;
        }
        if (k > 0) {
            for (TreeNode* adj : graph[node]) {
                if (seen.find(adj) == seen.end()) {
                    dfs2(adj, k-1);
                }
            }
        }
    }

    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        dfs(root);
        dfs2(target, k);
        return ans;
    }
};