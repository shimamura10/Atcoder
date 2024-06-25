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

template <typename T>
class SegmentTree
{
private:
    int _valueNum;  // 要素数
    int _initVal;  // セグ木の初期値
    int _leafNum = 1;  // セグ木の葉の数
    vector<T> _tree;
    function<T(T, T)> _segfunc;
public:
    SegmentTree(vector<T>&& initVals, T initVal, function<T(T, T)> segfunc)
    {
        _valueNum = initVals.size();
        _initVal = initVal;
        int n = _valueNum;
        while (n != 0)
        {
            _leafNum *= 2;
            n /= 2;
        }
        _tree = vector<T>(_leafNum*2, _initVal);
        for (int i = 0; i < _valueNum; i++)
        {
            _tree[i+_leafNum] = initVals[i];
        }
        for (int i = _leafNum-1; i > 0; i--)
        {
            _tree[i] = segfunc(_tree[2*i], _tree[2*i+1]);
        }
        _segfunc = segfunc;
    };

    // k番目の要素をxに更新
    void update(int k, T x)
    {
        k += _leafNum;
        _tree[k] = x;
        while (k > 2)
        {
            k /= 2;
            _tree[k] = _segfunc(_tree[2*k], _tree[2*k+1]);
        }
    }

    // k番目の要素にxを加算
    void add(int k, T x)
    {
        k += _leafNum;
        _tree[k] += x;
        while (k > 2)
        {
            k /= 2;
            _tree[k] = _segfunc(_tree[2*k], _tree[2*k+1]);
        }
    }

    // l以上r未満番目の要素に対してsegfuncを実行した結果を返す
    T query(int l, int r)
    {
        T res = _initVal;
        l = max(l, 0);
        r = min(r, _valueNum);

        l += _leafNum;
        r += _leafNum;
        while (l < r)
        {
            if (l & 1)  // 右側の子だったら回収
            {
                res = _segfunc(res, _tree[l]);
                l += 1;
            }
            if (r & 1)  // 左側の子だったら回収(rは計算対象に含まないことに注意)
            {
                res = _segfunc(res, _tree[r-1]);
            }
            // ひとつ上の階層に移動
            l /= 2;
            r /= 2;
        }
        return res;
    }
};

using smt = SegmentTree<ll>;

std::random_device seed_gen;
std::default_random_engine engine(seed_gen());


int main(){
    int cnt{0};
    for (int _=0; _<1; ++_){
    int N = 100000;
     // 0以上9以下の値を等確率で発生させる
    std::uniform_int_distribution<> dist(0, N);
    // vi A{1,2,3,4,0,6,0,8,10,9};
    vi A{};
    for (int i=0; i<N; ++i){
        A.push_back(dist(engine));
    }

    vi sortedA{};
    set<int> setA{};
    for (int i=0; i<N; ++i){
        if (setA.find(A[i]) != setA.end()) continue;
        sortedA.push_back(A[i]);
        setA.insert(A[i]);
    }
    sort(sortedA.begin(), sortedA.end());
    unordered_map<int, int> orderA{};
    for (int i=0; i<sortedA.size(); ++i){
        orderA[sortedA[i]] = i;
    }

    ll ans{0};
    for (ll i=0; i<N; ++i){
        ans += (i*2+1-N)*A[i];
    }

    // cout << ans << endl;

    smt segtree(vector<ll>(N, 0LL), 0, [](ll a, ll b){return a+b;});
    smt segtree2(vector<ll>(N, 0LL), 0, [](ll a, ll b){return a+b;});
    for (int i=N-1; i>=0; --i){
        // cout << "ord[i]:" << orderA[A[i]] << endl;
        ans += A[i] * segtree2.query(0, orderA[A[i]]);
        // cout << "seg2:" << segtree2.query(0, orderA[A[i]]) << endl;
        segtree2.add(orderA[A[i]], 1);

        ans -= segtree.query(0, orderA[A[i]]);
        // cout << "seg:" << segtree.query(0, orderA[A[i]]) << endl;
        segtree.add(orderA[A[i]], A[i]);

        // cout << ans << endl;
    }

    ll ans2{0};
    for (int i=0; i<N; ++i){
        for (int j=i+1; j<N; ++j){
            ans2 += max(0, A[j]-A[i]);
        }
    }

    if (ans != ans2){
        cout << "---------------------" << endl;
        cout << _ << endl;
        ++cnt;
        cout << "N: "<< N << endl;
        cout << "A: ";
        // for (int i=0; i<N; ++i){
        //     cout << A[i] << " ";
        // }
        cout << endl;
        cout << "ans: " << ans << endl;
        cout << "ans2: " << ans2 << endl;
    } 
    }
    cout << "cnt: " << cnt << endl;
}