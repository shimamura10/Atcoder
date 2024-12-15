#include<bits/stdc++.h>
using namespace std;

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

int main() {
    int N, M, K;
    cin >> N >> M >> K;
    vector<array<int, 3>> edges;
    for (int i=0; i<M; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        u--; v--;
        edges.push_back({w, u, v});
    }
    // idxを根とするグループが持つAの数を正で、Bの数を負で持つ
    vector<long long> cnt(N, 0);
    for (int i=0; i<K; i++) {
        int a;
        cin >> a;
        cnt[a-1]++;
    }
    for (int i=0; i<K; i++) {
        int b;
        cin >> b;
        cnt[b-1]--;
    }
    sort(edges.begin(), edges.end(), [](auto a, auto b) { 
        return a[0] < b[0]; 
    });
    UnionFind uf(N);
    long long ans = 0;
    for (auto [w, u, v] : edges) {
        if (uf.same(u, v)) { continue; }
        auto cntu = cnt[uf.find(u)];
        auto cntv = cnt[uf.find(v)];
        if (cntu * cntv < 0) {
            ans += w * min(abs(cntu), abs(cntv));
        }
        uf.unite(u, v);
        cnt[uf.find(u)] = cntu + cntv;
    }
    cout << ans << endl;
    return 0;
}
