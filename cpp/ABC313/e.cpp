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

int main(){
    int N;
    cin >> N;
    string S;
    cin >> S;
    const ll MOD = 998244353;
    ll ans{0};

    // Sに1以外の数字が連続した箇所があったら終了
    for (int i = 0; i < N-1; i++) {
        if (S[i] != '1' && S[i+1] != '1') {
            cout << -1 << endl;
            return 0;
        }
    }

    // Sの末尾の連続した1の数を求める
    for (int i = N-1; i >= 0; i--) {
        if (S[i] == '1') {
            ans++;
        } else {
            break;
        }
    }

    for (int i = N-1; i >= 0; i--) {
        if (S[i] != '1') {
            // Sの初めの数が1でない場合
            if (i == 0) {
                ans++;
                break;
            }

            ll cnt{0};
            while (S[i-cnt-1] == '1') {
                cnt++;
            }

            ll numSi = static_cast<ll>(S[i] - '0');
            // Sの末尾がS[i]になったときのS[i]の左に連続した1の数
            ll tmp = cnt + ans*(numSi - 1LL)%MOD;
            // S[i]の左に連続している1がなくなるまでの操作回数を足す
            ans += tmp + numSi;
            ans %= MOD;
        }
    }

    cout << ans - 1 << endl;
}