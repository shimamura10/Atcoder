#include <iostream>

long long cmb(int n, int r) {
    long long ans = 1;
    for (int i=0; i<r; i++) {
        ans *= n-i;
        ans /= i+1;
    }
    return ans;
}

int main() {
    // 21! = 51090942171709440000
    std::cout << cmb(21, 9) << std::endl;
}