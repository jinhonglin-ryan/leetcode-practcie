class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while (x) {
            int digit = x % 10;
            x /= 10;
            res = res * 10 + digit;
        }
        
        if (res > INT_MAX or res < INT_MIN) return 0;
        return res;
    }
};