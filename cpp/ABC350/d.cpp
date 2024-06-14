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
    ll N, M;
    cin >> N >> M;
    UnionFind uft(N);
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        uft.unite(a-1, b-1);
    }
    ll ans{0LL};
    for (int i=0; i<N; i++) {
        if (i == uft.find(i)) {
            ll size{uft.size(i)};
            ans += size*(size-1)/2;
        }
    }
    ans -= M;
    cout << ans;
}