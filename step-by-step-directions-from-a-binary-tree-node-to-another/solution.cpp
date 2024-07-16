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
    string getDirections(TreeNode* root, int startValue, int destValue) {
        unordered_map<TreeNode*, TreeNode*> par;
        unordered_map<TreeNode*, int> depth;
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* a = nullptr;
        TreeNode* b = nullptr;
        int d = 0;
        
        while (a == nullptr || b == nullptr) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                TreeNode* x = q.front();
                q.pop();
                depth[x] = d;
                if (x->val == startValue) a = x;
                if (x->val == destValue) b = x;
                if (x->left) {
                    q.push(x->left);
                    par[x->left] = x;
                }
                if (x->right) {
                    q.push(x->right);
                    par[x->right] = x;
                }
            }
            d++;
        }
        
        int c = 0;
        string st;
        
        while (a != b) {
            if (depth[a] < depth[b]) {
                if (par[b]->left == b) {
                    st += "L";
                } else {
                    st += "R";
                }
                b = par[b];
            } else if (depth[b] < depth[a]) {
                a = par[a];
                c++;
            } else {
                if (par[b]->left == b) {
                    st += "L";
                } else {
                    st += "R";
                }
                b = par[b];
                a = par[a];
                c++;
            }
        }
        
        string ans(c, 'U');
        reverse(st.begin(), st.end());
        ans += st;
        return ans;
    }
};