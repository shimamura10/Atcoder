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
    vl A;
    for (int i=0; i<N; ++i){
        ll a;
        cin >> a;
        A.push_back(a);
    }
    vl ans{};
    for (const auto& a : A){
        ans.push_back(a);
        while (ans.size() > 1 && ans[ans.size()-2] == ans.back()) {
            auto last = ans.back();
            ans.pop_back();
            ans.pop_back();
            ans.push_back(last+1);
        }
    }
    cout << ans.size() << endl;
}