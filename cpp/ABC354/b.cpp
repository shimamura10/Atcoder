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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

bool scomp(const string& a, const string& b) {
    auto mlen{ min(a.length(), b.length()) };
    for (int i=0; i<mlen; i++) {
        auto numa = static_cast<int> (a[i]);
        auto numb = static_cast<int> (b[i]);
        if (numa < numb) {
            return true;
        } else if (numa > numb) {
            return false;
        }
    }
    return a.length() < b.length();
}

int main(){
    int N;
    cin >> N;
    vector<string> S;
    int rate{0};
    for (int i=0; i<N; i++) {
        string s;
        int c;
        cin >> s >> c;
        S.emplace_back(s);
        rate += c;
    }
    sort(S.begin(), S.end(), scomp);
    cout << S[rate%N] << endl;
}