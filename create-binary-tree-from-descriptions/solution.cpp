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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_set<int> s;
        unordered_map<int, TreeNode*> nodes;

        for (const auto& desc : descriptions) {
            int x = desc[0];
            int y = desc[1];

            s.insert(y);

            if (nodes.find(y) == nodes.end()) {
                nodes[y] = new TreeNode(y);
            }

            if (nodes.find(x) == nodes.end()) {
                nodes[x] = new TreeNode(x);
            }

            if (desc[2]) {
                nodes[x]->left = nodes[y];
            } else {
                nodes[x]->right = nodes[y];
            }
        }

        for (auto it = nodes.begin(); it != nodes.end(); ++it) {
            if(s.find(it->first) == s.end()){
                int root = it->first;
                nodes[root]->val = root;
                return nodes[root];
            }
        }
        return new TreeNode();
    }
};