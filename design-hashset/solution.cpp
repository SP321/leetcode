class MyHashSet {
public:
    int tablesize=1e4*10/7;
    vector<list<int>> hashtable;
    MyHashSet() {
        hashtable.resize(tablesize);
    }
    void add(int key) {
        int hashValue = key % tablesize;
        for(auto &element : hashtable[hashValue]){
            if(element == key)
                return;
        }
        hashtable[hashValue].push_back(key);
    }
    
    void remove(int key) {
        int hashValue = key % tablesize;
        hashtable[hashValue].remove(key);
    }
    
    bool contains(int key) {
        int hashValue = key % tablesize;
        for(auto &element : hashtable[hashValue]){
            if(element == key)
                return true;
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */