#include<bits/stdc++.h>
using namespace std;

#include<atcoder/lazysegtree>
#include<atcoder/modint>
using namespace atcoder;

int M;
struct S { int value; int size; };
S op(S a, S b) { 
    S ret{
        a.value + b.value,
        a.size + b.size
    };
    return ret; 
}
S e() { return {0, 0}; }
S mapping(int f, S x) { 
    S ret{
        (x.value + x.size*f)%M, 
        x.size
    };
    return ret; 
}
int composition(int f, int g) { return (f + g)%M; }
int id() { return 0; }

void solve(int N, int M, vector<int>& A) {
    vector<S> init_vals(N, {0, 1});
    lazy_segtree<S, op, e, int, mapping, composition, id> seg(init_vals);
    long long ans = 0;
    for (int i=0; i<N; i++) {
        seg.apply(0, i+1, A[i]);
        for (int j=0; j<N; j++) {
            cout << seg.get(j).value << " ";
        }
        cout << endl;
        for (int j=0; j<N; j++) {
            cout << seg.get(j).size << " ";
        }
        cout << endl;
        auto tmp = seg.all_prod();
        cout << tmp.value << " " << tmp.size << endl;
        S tmp2 = e();
        for (int j=0; j<N; j++) {
            auto s = seg.get(j);
            tmp2 = op(tmp2, seg.get(j));
        }
        cout << tmp2.value << " " << tmp2.size << endl;
        
        ans += seg.prod(0, N).value;
    }
    cout << ans << endl;
}

int main() {
    int N;
    cin >> N >> M;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    solve(N, M, A);
    return 0;
}