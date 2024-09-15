const int INF = 1e9;

class Vertex {
public:
    unordered_map<char, Vertex*> next;  // Transitions to child nodes (dictionary of children)
    Vertex* parent;                     // Reference to the parent vertex
    char pch;                           // Character leading to this vertex from its parent
    Vertex* link;                       // Suffix link (failure link)
    unordered_map<char, Vertex*> go;    // Transitions to child nodes (using dictionaries)
    int ln;                             // Length of the string ending at this vertex

    Vertex(Vertex* parent = nullptr, char ch = '$', int ln = 0)
        : parent(parent), pch(ch), link(nullptr), ln(ln) {}
};

class AhoCorasick {
public:
    Vertex* root;

    AhoCorasick(const vector<string>& words) {
        root = new Vertex();
        for (const auto& word : words) {
            add_string(word);
        }
    }

    void add_string(const string& word) {
        Vertex* node = root;
        for (int i = 0; i < word.length(); ++i) {
            char ch = word[i];
            if (node->next.find(ch) == node->next.end()) {
                node->next[ch] = new Vertex(node, ch, i + 1);
            }
            node = node->next[ch];
        }
    }

    Vertex* get_link(Vertex* node) {
        if (node->link == nullptr) {
            if (node == root || node->parent == root) {
                node->link = root;
            } else {
                node->link = go(get_link(node->parent), node->pch);
            }
        }
        return node->link;
    }

    Vertex* go(Vertex* node, char ch) {
        if (node->go.find(ch) == node->go.end()) {
            if (node->next.find(ch) != node->next.end()) {
                node->go[ch] = node->next[ch];
            } else {
                node->go[ch] = (node == root) ? root : go(get_link(node), ch);
            }
        }
        return node->go[ch];
    }

    vector<pair<int, int>> iter_matches(const string& sentence) {
        vector<pair<int, int>> matches;
        Vertex* node = root;
        for (int i = 0; i < sentence.length(); ++i) {
            node = go(node, sentence[i]);
            if (node->ln > 0) {
                matches.push_back({i, node->ln});
            }
        }
        return matches;
    }
};

class Solution {
public:
    int minValidStrings(vector<string>& words, const string& target) {
        AhoCorasick tr(words);
        int n = target.size();
        vector<int> dp(n + 1, INF);
        dp[0] = 0;

        auto matches = tr.iter_matches(target);
        for (auto& [i, ln] : matches) {
            dp[i + 1] = min(dp[i + 1], dp[i + 1 - ln] + 1);
        }

        return dp[n] != INF ? dp[n] : -1;
    }
};