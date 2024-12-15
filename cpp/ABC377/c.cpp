#include<bits/stdc++.h>
using namespace std;

// pair<int, int> はハッシュ化できないので、自作のハッシュ関数を定義する
struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (std::pair<T1, T2> const &pair) const {
        std::size_t h1 = std::hash<T1>{}(pair.first);
        std::size_t h2 = std::hash<T2>{}(pair.second);
        return h1 ^ h2;
    }
};

int main() {
    long long N, M;
    cin >> N >> M;
    // unordered_set<pair<int, int>, pair_hash> ngs;
    unordered_set<long long> ngs;
    vector<pair<int, int>> ds = {{2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        // ngs.emplace(a, b);
        ngs.emplace(a*N + b);
        for (auto d : ds) {
            int x = a + d.first;
            int y = b + d.second;
            if (x < 0 || x >= N || y < 0 || y >= N) continue;
            // ngs.emplace(x, y);
            ngs.emplace(x*N + y);
        }
    }
    cout << N*N - ngs.size() << endl;
}