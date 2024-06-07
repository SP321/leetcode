class TrieNode {
public:
    unordered_map<char, shared_ptr<TrieNode>> children;
    string word;

    TrieNode() : word("") {}
};

class Trie {
public:
    shared_ptr<TrieNode> root;

    Trie() {
        root = make_shared<TrieNode>();
    }

    void add(const string& word) {
        shared_ptr<TrieNode> cur_node = root;
        for (char ch : word) {
            if (cur_node->children.find(ch) == cur_node->children.end()) {
                cur_node->children[ch] = make_shared<TrieNode>();
            }
            cur_node = cur_node->children[ch];
        }
        cur_node->word = word;
    }

    string search(const string& word) {
        shared_ptr<TrieNode> cur_node = root;
        for (char ch : word) {
            if (cur_node->children.find(ch) == cur_node->children.end()) {
                return word;
            }
            cur_node = cur_node->children[ch];
            if (!cur_node->word.empty()) {
                return cur_node->word;
            }
        }
        return word;
    }
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        Trie trie;
        for (const string& word : dictionary) {
            trie.add(word);
        }

        stringstream ss(sentence);
        string token;
        string result;
        bool firstWord = true;

        while (getline(ss, token, ' ')) {
            if (!firstWord) result += " ";
            result += trie.search(token);
            firstWord = false;
        }
        return result;
    }
};