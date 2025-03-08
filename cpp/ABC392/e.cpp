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
    int N, M;
    cin >> N >> M;
    UnionFind uf(N);
    vector<vector<int>> amari{};
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        if (uf.same(a, b)) {
            amari.push_back({a, b, i});
        } else {
            uf.unite(a, b);
        }
    }

    unordered_set<int> roots{};
    for (int i=0; i<N; i++) {
        roots.insert(uf.find(i));
    }

    vector<vector<int>> ans{};
    for (const auto& edge : amari) {
        for (const auto& root : roots) {
            if (!uf.same(edge[0], root)) {
                uf.unite(edge[0], root);
                ans.push_back({edge[2], edge[0], root});
                roots.erase(root);
                break;
            }
        }
    }

    cout << ans.size() << endl;
    for (const auto& a : ans) {
        cout << a[0]+1 << " " << a[1]+1 << " " << a[2]+1 << endl;
    }
    return 0;
}