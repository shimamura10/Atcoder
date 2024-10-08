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
            if (l & 1)  // lが右側の子だったら回収
            {
                res = _segfunc(res, _tree[l]);
                l += 1;
            }
            if (r & 1)  // r-1が左側の子だったら回収(rは計算対象に含まないことに注意)
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

int main(){
    int N, Q;
    cin >> N >> Q;
    string S;
    cin >> S;
    SegmentTree<bool> segtree(vector<bool>(N-1, false), true, [](bool a, bool b){return a && b;});
    for (int i = 0; i < N-1; i++)
    {
        if (S[i] != S[i+1])
        {
            segtree.update(i, true);
        }
    }

    for (int i = 0; i < Q; i++)
    {
        int t, l, r;
        cin >> t >> l >> r;
        l--;
        r--;
        if (t == 1)
        {
            if (l > 0)
            {
                segtree.update(l-1, !segtree.query(l-1, l));
            }
            if (r < N-1)
            {
                segtree.update(r, !segtree.query(r, r+1));
            }
        }
        else
        {
            if (segtree.query(l, r))
            {
                cout << "Yes" << endl;
            }
            else
            {
                cout << "No" << endl;
            }
        }
    }
}