class SmallestInfiniteSet {
public:
    int i;
    set<int> s;
    SmallestInfiniteSet() {
        i = 1;
    }
    int popSmallest() {
        if (!s.empty()) {
            int result = *s.begin();
            s.erase(s.begin());
            return result;
        }
        return i++;
    }
    
    void addBack(int num) {
        if (num < i) 
            s.insert(num);
    }
};
