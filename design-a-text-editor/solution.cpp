class TextEditor {
private:
    vector<char> x;
    vector<char> y;

public:
    TextEditor() {}

    void addText(const string& text) {
        for (char c : text) {
            x.push_back(c);
        }
    }

    int deleteText(int k) {
        int deleted = 0;
        for (int i = 0; i < k; ++i) {
            if (x.empty()) {
                return deleted;
            }
            x.pop_back();
            ++deleted;
        }
        return deleted;
    }

    string cursorLeft(int k) {
        for (int i = 0; i < k; ++i) {
            if (x.empty()) {
                break;
            }
            y.push_back(x.back());
            x.pop_back();
        }
        return getLast10Characters();
    }

    string cursorRight(int k) {
        for (int i = 0; i < k; ++i) {
            if (y.empty()) {
                break;
            }
            x.push_back(y.back());
            y.pop_back();
        }
        return getLast10Characters();
    }

private:
    string getLast10Characters() {
        string ans;
        int start = max(0, (int)(x.size()) - 10);
        for (int i = start; i < x.size(); ++i) {
            ans += x[i];
        }
        return ans;
    }
};
/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */