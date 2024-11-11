auto primes = []() {
    int n=8000;
    int p = 3;
    int sieve[n+1];
    for (int i = 0; i <= n; ++i) sieve[i] = 1;
    while (p * p <= n) {
        if (sieve[p]) {
            for (int x = p * p; x <= n; x += 2 * p) {
                sieve[x] = 0;
            }
        }
        p += 2;
    }
    int primes[8001];
    int idx = 0;
    primes[idx++] = 2;
    for (int i = 3; i <= n; i += 2) {
        if (sieve[i]) {
            primes[idx++] = i;
        }
    }
    return vector<int>(primes, primes + idx);
}();

class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        int n = nums.size();
        
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] > nums[i + 1]-1) {
                int diff = nums[i] - (nums[i + 1] - 1);
                nums[i] -= *lower_bound(primes.begin(),primes.end(),diff);
                if (nums[i] <= 0) {
                    return false;
                }
            }
        }
        return true;
    }
};
