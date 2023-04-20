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

    int widthOfBinaryTree(TreeNode* root) {
        vector<TreeNode*>x={root};
        map<TreeNode*,long long>m;
        int ans=0;
        m[root]=0;
        while(x.size()){
            vector<TreeNode*>y;
            int minm=0;
            int i=0;
            while (i<x.size()){
                TreeNode*a=x[i];
                if(a->left){
                    minm=2*m[a];
                    break;
                }
                if(a->right){
                    minm=2*m[a]+1;
                    break;
                }
                i++;
            }
            while (i<x.size()){
                TreeNode*a=x[i];
                if(a->left){
                    y.push_back(a->left);
                    m[a->left]=m[a]*2 -minm;
                    ans=max(ans,(int)m[a->left]);
                }
                if(a->right){
                    y.push_back(a->right);
                    m[a->right]=m[a]*2+1 -minm;
                    ans=max(ans,(int)m[a->right]);
                }
                i++;
            }
            x=y;
        }
        return ans+1;
    }
};