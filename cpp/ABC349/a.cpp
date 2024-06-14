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
using namespace std;
using vi = vector<int>;

int main(){
    int N;
    cin >> N;
    int s{0};
    for (int i=0; i<N-1; i++) {
        int a;
        cin >> a;
        s += a;
    }
    cout << -s;
}