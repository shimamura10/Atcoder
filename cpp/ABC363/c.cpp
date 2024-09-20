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
const int MOD = 998244353;


int main(){
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    sort(S.begin(), S.end());
    int ans{0};
    do {
        bool haskaibun = false;
        for (int i = 0; i < N - K + 1; ++i){
            bool iskaibun = true;
            for (int j = 0; j < K/2; ++j){
                if (S[i+j] != S[i+K-1-j]){
                    iskaibun = false;
                    break;
                }
            }
            if (iskaibun){
                haskaibun = true;
                break;
            }
        }
        if (!haskaibun){
            ++ans;
        }
    } while(next_permutation(S.begin(), S.end()));

    cout << ans << endl;
}