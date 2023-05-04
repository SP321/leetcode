template<typename T>
class FenwickTree {
public:
    FenwickTree(int size) : size(size), tree(size + 1, 0) {}

    void update(int i, T delta) {
        while (i <= size) {
            tree[i] += delta;
            i += lsb(i);
        }
    }
    
    void update_value(int i, T value) {
        T old_value = prefix_sum(i) - prefix_sum(i - 1);
        T delta = value - old_value;
        update(i, delta);
    }

    T prefix_sum(int i) {
        T total = 0;
        while (i > 0) {
            total += tree[i];
            i -= lsb(i);
        }
        return total;
    }

    T range_sum(int i, int j) {
        return prefix_sum(j) - prefix_sum(i - 1);
    }

    void print_elements() {
        for (int i = 1; i <= size; ++i) {
            std::cout << prefix_sum(i) - prefix_sum(i - 1) << " ";
        }
        std::cout << std::endl;
    }

private:
    int size;
    std::vector<T> tree;

    int lsb(int i) {
        return i & -i;
    }
};
class NumArray {
public:
    FenwickTree<int>*ft;
    int n;
    NumArray(vector<int>& nums) {
        n=nums.size();
        ft=new FenwickTree<int>(n);
        for(int i=0;i<n;i++)
            ft->update(i+1,nums[i]);
    }
    
    void update(int index, int val) {
        ft->update_value(index+1,val);
    }
    
    int sumRange(int left, int right) {
        return ft->range_sum(left+1,right+1);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */