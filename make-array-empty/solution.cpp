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

class Solution {
public:
    long long countOperationsToEmptyArray(vector<int>& nums) {
        int n=nums.size();
        vector<int>a(n);
        for(int i=0;i<n;i++)
            a[i]=i;
        sort(a.begin(),a.end(),[&nums](int x,int y){return nums[x]<nums[y];});
        FenwickTree<uint64_t>count_op(n);
        for(int i=0;i<n;i++)
            count_op.update(i+1,1);
        long long ans=0;
        int curpos=0;
        for(int i=0;i<n;i++){
            int j=a[i];
            if(j<curpos){
                ans+=count_op.range_sum(curpos+1,n);
                ans+=count_op.range_sum(1,j+1);
            }else
                ans+=count_op.range_sum(curpos+1,j+1);
            count_op.update(j+1,-1);
            curpos=j;
        }
        return ans;
    }
};