class Solution
{
public:
      TreeNode *replaceValueInTree(TreeNode *root)
      {
            dfs(root, nullptr, 0);
            calculate(root, nullptr, 0);
            update(root);
            return root;
      }

      map<int, int> depth_sum;
      map<TreeNode *, TreeNode *> parent;
      map<TreeNode *, int> new_vals;

      void dfs(TreeNode *node, TreeNode *p, int depth)
      {
            if (!node)
            {
                  return;
            }
            depth_sum[depth] += node->val;
            parent[node] = p;
            dfs(node->left, node, depth + 1);
            dfs(node->right, node, depth + 1);
      }

      void calculate(TreeNode *node, TreeNode *p, int depth)
      {
            if (!node)
            {
                  return;
            }

            int sum = depth_sum[depth];
            if (parent[node])
            {
                  if (parent[node]->left)
                        sum -= parent[node]->left->val;
                  if (parent[node]->right)
                        sum -= parent[node]->right->val;
            }
            else
                  sum -= node->val;

            new_vals[node] = sum;

            calculate(node->left, node, depth + 1);
            calculate(node->right, node, depth + 1);
      }

      void update(TreeNode *node)
      {
            if (!node)
            {
                  return;
            }
            node->val = new_vals[node];
            update(node->left);
            update(node->right);
      }
};