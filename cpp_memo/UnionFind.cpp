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

struct UnionFind 
{
    // 親ノード
    vector<int> parents;
    // それが根である場合は自身の木のサイズ
    vector<int> sizes;

    // N:union findのサイズ
    UnionFind(int N) {
        parents.assign(N, -1);
        sizes.assign(N, 1);
        for (int i=0; i<N; i++) {
            parents[i] = i;
        }
    }

    // 根を返す
    int find(int x) {
        if (x == parents[x]) { return x; }
        return parents[x] = find(parents[x]);
    }

    // 同じ木に属していたら何もせずfalseを返す
    // 異なる木に属していたらマージしてtrueを返す
    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) { return false; }
        if (sizes[x] < sizes[y]) { swap(x, y); }
        parents[y] = x;
        sizes[x] += sizes[y];
        return true;
    }

    // xとyが同じ木に属しているか
    bool same(int x, int y) {
        return find(x) == find(y);
    }

    // それを含む木のサイズを返す
    int size(int x) {
        return sizes[find(x)];
    }
};

int main(){
    std::random_device seed_gen;
    std::default_random_engine engine(seed_gen());
    int N = 20;
    UnionFind uft(N);
    std::uniform_int_distribution<> dist(0, N-1);
    while (true) {
        string s;
        cin >> s;
        cout << "---------------------" << endl;
        if (s == "q") {return 0;}
        int x{dist(engine)}, y{dist(engine)};
        uft.unite(x, y);
        cout << "unite(" << x << ", " << y << ")" << endl;
        cout << "根ノード" << endl;
        for (int i=0; i<N; i++) {
            cout << i << ":" << uft.find(i) << " ";
        }
        cout << endl;
        cout << "サイズ" << endl;
        for (int i=0; i<N; i++) {
            cout << i << ":" << uft.size(i) << " ";
        }
        cout << endl;
        cout << "--------------------" << endl;
    }
}