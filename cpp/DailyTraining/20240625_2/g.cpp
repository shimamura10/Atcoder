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
const ll MOD = 998244353;

struct UnionFind 
{
    // 親ノード
    vector<int> parents;
    // それが根である場合は自身の木のサイズ
    vector<int> sizes;
    // グループ数
    int group;

    // N:union findのサイズ
    UnionFind(int N) {
        parents.assign(N, -1);
        sizes.assign(N, 1);
        group = N;
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
        group -= 1;
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
    int N, M;
    cin >> N >> M;
    UnionFind uf(N);
    vector<pair<int, int>> loop_edges;
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        if (uf.same(a, b)) {
            loop_edges.push_back({a, b});
        } else {
            uf.unite(a, b);
        }
    }
    vector<bool> flags(N, false);
    if (loop_edges.size() != uf.group) {
        cout << "No" << endl;
        return 0;
    }
    for (const auto& e : loop_edges) {
        if (flags[uf.find(e.first)] == false) {
            flags[uf.find(e.first)] = true;
            continue;
        } else {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
}