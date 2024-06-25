#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <functional>
using namespace std;

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
    SegmentTree(vector<T>& initVals, T initVal, function<T(T, T)> segfunc)
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

int main(){
    int N, D;
    cin >> N >> D;
    int MAX_A = 5*static_cast<int>(pow(10,5));
    vector<int> initVals(MAX_A+1, 0);
    SegmentTree<int> segmentTree(initVals, 0,
        [](int x, int y) { return max(x,y); }
    );
    vector<int> A;
    for (size_t i = 0; i < N; i++)
    {
        int a;
        cin >> a;
        int tmpMax;
        tmpMax = segmentTree.query(a-D, a+D+1);
        segmentTree.update(a, tmpMax+1);
    }

    cout << segmentTree.query(0,MAX_A+1);
}