#include<bits/stdc++.h>
using namespace std;

vector<long long> primaryList(long long n) {
    vector<long long> res;
    vector<bool> is_prime(n+1, true);
    is_prime[0] = is_prime[1] = false;
    for (long long i = 2; i <= n; i++) {
        if (is_prime[i]) {
            res.push_back(i);
            for (long long j = 2*i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    return res;
}

int main() {
    long long N;
    cin >> N;
    long long sqrtN = sqrt(N);
    auto primes = primaryList(sqrtN);
    long long ans = 0;
    for (int i = 0; i < primes.size(); i++) {
        int j = upper_bound(primes.begin(), primes.end(), sqrtN/primes[i]) - primes.begin();
        ans += max(0, j - i - 1);
    }
    for (const auto prime : primes) {
        if (pow(prime, 8) <= N) {
            ans++;
        } else {
            break;
        }
    }
    cout << ans << endl;
}