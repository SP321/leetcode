/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> ans;
        function<void(Node*)> dfs = [&](Node* node) {
            if (!node) return;
            for (Node* n2 : node->children) {
                dfs(n2);
            }
            ans.push_back(node->val);
        };
        dfs(root);
        return ans;
    }
};