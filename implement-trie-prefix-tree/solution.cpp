
class TrieNode {
public:
    vector<TrieNode*> children;
    bool end;

    TrieNode() : children(26, nullptr), end(false) {}
};

class Trie {
private:
    TrieNode* root;

    TrieNode* traverse(const string& word, bool create = false) {
        TrieNode* cur = root;
        for (char c : word) {
            int i = c - 'a';
            if (!cur->children[i]) {
                if (!create) {
                    return nullptr;
                }
                cur->children[i] = new TrieNode();
            }
            cur = cur->children[i];
        }
        return cur;
    }

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(const string& word) {
        TrieNode* node = traverse(word, true);
        node->end = true;
    }

    bool search(const string& word) {
        TrieNode* node = traverse(word);
        return node && node->end;
    }

    bool startsWith(const string& prefix) {
        return traverse(prefix) != nullptr;
    }

};
/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */