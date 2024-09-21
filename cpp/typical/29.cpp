#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const int MOD = 998244353;

// 普通のセグ木のグラフ (d)ノードの型
using S = int;
// 遅延用のグラフ (lz)の型
using F = int;
// 区間取得用の関数。普通のセグ木と同じ
S op(S a, S b) { return max(a, b); }
// dの初期値。単位元である。op(a, e()) = a が成り立つ。
S e(){ return -1; }
// dを更新するときの関数。遅延は上から下に伝播するので、一階層下のdにfを適用する。
S mapping(F f, S x) { return max(f, x); }
// lzを更新するときの関数。fは一階層下のdに適用されるので、fは遅延されていた更新をすべて吸収しておく必要がある。そのため二つの作用fの合成を定義する。
F composition(F f, F g) { return max(f, g); }
// lzの初期値。恒等関数である必要がある。
F id() { return -1; }

int main(){
    int W, N;
    cin >> W >> N;
    vi init_val(W, 0);
    atcoder::lazy_segtree<S, op, e, F, mapping, composition, id> seg(init_val);
    for (int i = 0; i < N; ++i) {
        int l, r;
        cin >> l >> r;
        --l;
        int h = seg.prod(l, r)+1;
        cout << h << endl;
        seg.apply(l, r, h);
    }
}