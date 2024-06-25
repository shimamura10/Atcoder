#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <unordered_map>
#include <memory>
#include <queue>
#include <unordered_set>
#include <limits>
#include <tuple>
#include <numeric>
#include <set>
#include <random>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

std::random_device seed_gen;
std::default_random_engine engine(seed_gen());

int main(){
    for (int _=0; _<1000; _++) {
    // input generate
    int N = 10;
    int K = 3;
    vi P;
    for (int i=1; i<=N; i++) {
        P.emplace_back(i);
    }
    shuffle(P.begin(), P.end(), engine);

    // ans1
    int ans1{1001};
    int m1, M1;
    unordered_map<int, int> pos;
    for (int i=0; i<N; i++) {
        int p{P[i]};
        // P.emplace_back(p);
        pos[p] = i;
    }

    set<int> s;
    for (int i=1; i<K; i++) {
        s.insert(pos[i]);
    }

    for (int i=K; i<=N; i++) {
        s.insert(pos[i]);
        auto tmp = *s.rbegin() - *s.begin();
        if (ans1 > tmp) {
            ans1 = tmp;
            m1 = *s.begin();
            M1 = *s.rbegin();
        }
        s.erase(pos[i-K+1]);
    }

    // ans2
    int ans2{1000};
    int m2, M2, num;
    for (int i=1; i<=N-K+1; i++) {
        int m{1000};
        int M{-1};
        for (int j=0; j<K; j++) {
            int ind{0};
            for (auto p : P) {
                if (p == i+j) {
                    break;
                }
                ind++;
            }
            m = min(m, ind);
            M = max(M, ind);
        }
        auto tmp = M-m;
        if (ans2 > tmp) {
            ans2 = tmp;
            m2 = m;
            M2 = M;
            num = i;
        }
        // ans2 = min(ans2, M-m);
    }

    if (ans1 != ans2) {
        cout << "N:" << N << endl;
        cout << "K:" << K << endl;
        cout << "P: ";
        for (auto p: P) {
            cout << p << " ";
        }
        cout << endl;
        cout << "ans1: " << ans1 << endl;
        cout << "m1: " << m1 << endl;
        cout << "M1: " << M1 << endl;
        cout << "ans2: " << ans2 << endl;
        cout << "m2: " << m2 << endl;
        cout << "M2: " << M2 << endl;
        cout << "num: " << num << endl;
        cout << "-----------------" << endl;
    }
    }
}