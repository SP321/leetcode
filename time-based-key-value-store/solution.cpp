class TimeMap {
public:
    map<string, vector<pair<int, string>>> m;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        m[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        pair<int, string> p = {timestamp, string({127})};
        auto i = upper_bound(m[key].begin(), m[key].end(), p);
        return (i != m[key].begin())?(i - 1)->second:"";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */