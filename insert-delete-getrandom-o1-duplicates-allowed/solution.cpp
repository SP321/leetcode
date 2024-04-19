class RandomizedCollection {
private:
    vector<int> a;
    unordered_map<int, unordered_set<int>> idx;

public:
    RandomizedCollection() {
        a.clear();
        idx.clear();
    }

    bool insert(int val) {
        idx[val].insert(a.size());
        a.push_back(val);
        return idx[val].size() == 1;
    }

    bool remove(int val) {
         if (idx[val].empty()) {
            return false;
        }
        auto remove_it = idx[val].begin();
        int remove = *remove_it;
        int last = a.back();
        a[remove] = last;
        idx[val].erase(remove_it);
        idx[last].insert(remove);
        idx[last].erase(a.size() - 1);
        a.pop_back();
        return true;
    }

    int getRandom() {
        return a[rand() % a.size()];
    }
};
