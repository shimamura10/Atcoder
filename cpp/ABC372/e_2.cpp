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

    int K=10;
    vector<vector<int>> topK;

    // N:union findのサイズ
    UnionFind(int N) {
        parents.assign(N, -1);
        sizes.assign(N, 1);
        group = N;
        for (int i=0; i<N; i++) {
            parents[i] = i;
        }
        topK.assign(N, vector<int>(K, -1));
        for (int i=0; i<N; i++) {
            topK[i][0] = i+1;
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

        int xi = 0, yi = 0;
        vector<int> tmp(K, -1);
        for (int i=0; i<K; i++) {
            if (topK[x][xi] > topK[y][yi]) {
                tmp[i] = topK[x][xi];
                xi++;
            } else {
                tmp[i] = topK[y][yi];
                yi++;
            }
        }
        topK[x] = tmp;
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

    int getKth(int x, int k) {
        return topK[find(x)][k-1];
    }
};

int main() {
    int N, Q;
    cin >> N >> Q;
    UnionFind uf(N);
    for (int i=0; i<Q; i++) {
        int t, u, v;
        cin >> t >> u >> v;
        if (t == 1) {
            uf.unite(u-1, v-1);
        } else {
            cout << uf.getKth(u-1, v) << endl;
        }
    }
}