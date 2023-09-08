class LRUCache {
public:
    LRUCache(int capacity) : _capacity(capacity) {}
    
    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;
        
        keys.splice(keys.begin(), keys, it->second.second);
        return it->second.first;
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if (it != cache.end()) {
            it->second.first = value;
            keys.splice(keys.begin(), keys, it->second.second);
            return;
        }
        
        if (cache.size() == _capacity) {
            int oldKey = keys.back();
            keys.pop_back();
            cache.erase(oldKey);
        }
        
        keys.push_front(key);
        cache[key] = {value, keys.begin()};
    }

    int _capacity;
    list<int> keys;
    unordered_map<int, pair<int, list<int>::iterator>> cache;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */