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
#include <string>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

struct InputCreator {
    std::default_random_engine _engine;
    InputCreator() {
        std::random_device seed_gen;
        _engine = std::default_random_engine(seed_gen());
    }

    // [a, b]の整数をランダムに生成
    int randint(int a, int b) {
        std::uniform_int_distribution<int> dist(a, b);
        return dist(_engine);
    }

    // 長さNで、[a, b]の要素を持つvectorを生成
    vi randints(int N, int a, int b) {
        vi res(N);
        for (int i=0; i<N; i++) {
            res[i] = randint(a, b);
        }
        return res;
    }
};

int response(const vi& A, vi& Q) {
    int res{0};
    for (const auto& q: Q) {
        res += A[q-1];
    }
    return res%2;
}

vi solve(const int N, const int K, const vi& A) {
    // if (N == K*2) 
    // { cout << "error" << endl; }
    vi Q(K, 0);
    for (int i=0; i<K; i++) {
        Q[i] = i+1;
    }
    int res0 = response(A, Q);
    int prev_res = res0;

    vector<vector<pair<int, int>>> edges(N);
    for (int i=0; i<K; i++) {
        int next = (i+K)%N;
        Q[i%K] = next+1;
        auto cur_res = response(A, Q);
        if (prev_res == cur_res) {
            edges[i].emplace_back(0,next);
            edges[next].emplace_back(0,i);
        } else {
            edges[i].emplace_back(1,next);
            edges[next].emplace_back(1,i);
        }
        prev_res = cur_res;
    }

    for (int i=0; i<K; i++) {
        Q[i] = i+1;
    }
    for (int i=K; i<N-1; i++) {
        int next = (1+i)%N;
        Q[0] = next+1;
        auto cur_res = response(A, Q);
        if (res0 == cur_res) {
            edges[0].emplace_back(0,next);
            edges[next].emplace_back(0,0);
        } else {
            edges[0].emplace_back(1,next);
            edges[next].emplace_back(1,0);
        }
    }
    
    vi ans(N, -1);
    ans[0] = 0;
    vi cand = {0};
    while (!cand.empty()) {
        int v = cand.back();
        cand.pop_back();
        for (auto& [d, u] : edges[v]) {
            if (ans[u] != -1) continue;
            else if (d == 0) ans[u] = ans[v];
            else ans[u] = 1 - ans[v];
            cand.push_back(u);
        }
    }

    int cnt0 = count(ans.begin(), ans.begin()+K, 0);
    if (cnt0%2 == res0) {
        for (auto& a: ans) {
            a = 1 - a;
        }
    }

    return ans;
};

int main(){
    for (int i=0; i<100; i++) {
        // 入力の作成
        InputCreator input_creator;
        int N = input_creator.randint(2, 10);
        int K = input_creator.randint(1, N-1);
        // int N{6}, K{3};
        if (K%2 == 0) {
            K--;
        }
        vi A = input_creator.randints(N, 0, 1);

        // 回答の作成
        auto ans = solve(N, K, A);

        // 間違ってたら出力
        if (ans.size() != A.size()) {
            cout << "size error" << endl;
        }
        for (int i=0; i<N; i++) {
            if (ans[i] != A[i]) {
                cout << "error" << endl;
                cout << "N: " << N << endl;
                cout << "K: " << K << endl;
                cout << "A: ";
                for (const auto& a: A) {
                    cout << a << " ";
                }
                cout << endl;
                cout << "ans: ";
                for (const auto& a: ans) {
                    cout << a << " ";
                }
                cout << endl;
                break;
            }
        }
    }
}