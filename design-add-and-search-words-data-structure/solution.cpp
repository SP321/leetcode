class TrieNode {
public:
    vector<TrieNode*> children;
    bool end;

    TrieNode() : children(26, nullptr), end(false) {}
};

class WordDictionary {

public:
    TrieNode* root;

    bool dfs(int i, const string& word, TrieNode* node) {
        if (i == word.size()) {
            return node->end;
        }

        if (word[i] != '.') {
            int index = word[i] - 'a';
            if (!node->children[index]) {
                return false;
            }
            return dfs(i + 1, word, node->children[index]);
        } else {
            for (TrieNode* child : node->children) {
                if (child && dfs(i + 1, word, child)) {
                    return true;
                }
            }
            return false;
        }
    }
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (!node->children[index]) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        node->end = true;
    }

    bool search(const string& word) {
        return dfs(0, word, root);
    }

};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */