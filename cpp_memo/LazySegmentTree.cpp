#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
using namespace std;

// https://betrue12.hateblo.jp/entry/2020/09/22/194541
// https://qiita.com/Kept1994/items/d156a1ac1fe28553bf94
// https://atcoder.github.io/ac-library/production/document_ja/lazysegtree.html

// 区間加算、区間最小
// 普通のセグ木のグラフ (d)ノードの型
using S = int;
// 遅延用のグラフ (lz)の型
using F = int;
// 区間取得用の関数。普通のセグ木と同じ
S op(S a, S b) { return min(a, b); }
// dの初期値。単位元である。op(a, e()) = a が成り立つ。
S e(){ return int(1e9)+1; }
// dを更新するときの関数。遅延は上から下に伝播するので、一階層下のdにfを適用する。
S mapping(F f, S x) { return f + x; }
// lzを更新するときの関数。fは一階層下のdに適用されるので、fは遅延されていた更新をすべて吸収しておく必要がある。そのため二つの作用fの合成を定義する。
F composition(F f, F g) { return f + g; }
// lzの初期値。恒等関数である必要がある。
F id() { return 0; }

int main() {
    vector<int> v(10, 0);
    // コンストラクタの引数は、要素数もしくは初期値のvector。要素数のときは初期値は単位元になる。
    atcoder::lazy_segtree<S, op, e, F, mapping, composition, id> seg(v);
    // [0, 5) の区間に 2 を加算
    seg.apply(0, 5, 2);
    // [3, 7) の区間に 3 を加算
    seg.apply(3, 7, 3);
    // [1, 4) の区間の最小値を取得
    cout << seg.prod(1, 4) << endl;
    // 全ての値を出力
    for (int i = 0; i < v.size(); ++i) {
        cout << seg.get(i) << " ";
    }
}