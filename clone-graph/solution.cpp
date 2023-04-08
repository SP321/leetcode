/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(node==nullptr)
            return nullptr;
        Node* ans=new Node(node->val);
        queue<Node*>q;
        map<Node*,Node*>cpy;
        map<Node*,int>seen;
        q.push(node);
        cpy[node]=ans;
        while(!q.empty()){
            Node* x=q.front();q.pop();
            Node* a=cpy[x];
            if(seen[x])
                continue;
            seen[x]=1;
            for(Node* y:x->neighbors){
                    q.push(y);
                    Node* b;
                    if(cpy[y])
                        b=cpy[y];
                    else{
                        b=new Node(y->val);
                        cpy[y]=b;
                    }
                    a->neighbors.push_back(b);
            }
        }
        return ans;
    }
};