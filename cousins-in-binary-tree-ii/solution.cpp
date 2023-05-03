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
class Solution
{
public:
        int maxdepth=0;
        map<int, long long> depth_sum;
        map<int, vector<TreeNode *>> depth_map;
        map<TreeNode *, TreeNode *> sibling;
        TreeNode *replaceValueInTree(TreeNode *root)
        {
                dfs(root, nullptr, 0);
                for(int i=0;i<=maxdepth;i++){
                    map<TreeNode *, int> new_vals;
                    for(auto &cur:depth_map[i]){
                        long long value=depth_sum[i]- cur->val;
                        TreeNode *s=sibling[cur];
                        if(s)
                            value-=s->val;
                        new_vals[cur]=value;
                    }
                    for(auto &cur:depth_map[i])
                        cur->val=new_vals[cur];
                }
                return root;
        }

        void dfs(TreeNode *node, TreeNode *p, int depth)
        {
                maxdepth=max(depth,maxdepth);
                depth_sum[depth] += node->val;
                depth_map[depth].push_back(node);
                if(node->left){
                    sibling[node->left]=node->right;
                    dfs(node->left, node, depth + 1);
                }
                if(node->right){
                    sibling[node->right]=node->left;
                    dfs(node->right, node, depth + 1);
                }
        }
        
};