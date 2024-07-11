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
using vi = vector<ll>;
using vvi = vector<vector<ll>>;
using vl = vector<long long>;

int main(){
    ll N;
    cin >> N;
    vi edges{};
    for (ll i=0; i<N; i++) {
        ll a;
        cin >> a;
        edges.emplace_back(a-1);
    }

    // iからいけるノードの数
    vi cnts(N, 0);
    vector<bool> visited(N, false);
    ll ans{0};

    // 出発点をiとして探索
    for (ll i=0; i<N; i++) {
        // 訪問済みならスキップ
        if (cnts[i] > 0) {
            continue;
        }
        ll next{i};

        // iから到達可能でまだ訪れていないところを見つける
        vi nowVisit{};
        while (!visited[next]) {
            visited[next] = true;
            nowVisit.emplace_back(next);
            next = edges[next];
        }

        // 円を見つけたら
        if (cnts[next] == 0) {
            for (ll j=0; j<nowVisit.size(); j++) {
                // 円の始め
                if (nowVisit[j] == next) {
                    // 円に含まれるもののcntsを更新
                    for (ll k=j; k<nowVisit.size(); k++) {
                        cnts[nowVisit[k]] = nowVisit.size() - j;
                    }
                    break;
                }
            }
        }

        // 発見したところのcntsを更新
        for (ll j=nowVisit.size()-1; j>=0; j--) {
            if (cnts[nowVisit[j]] > 0) {
                visited[nowVisit[j]] = true;
                continue;
            }
            cnts[nowVisit[j]] = cnts[edges[nowVisit[j]]] + 1;
            visited[nowVisit[j]] = true;
        }
    }

    for (const auto& c : cnts) {
        ans += c;
    }

    cout << ans;
}