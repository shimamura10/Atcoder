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

int main(){
    int N;
    cin >> N;
    for (int i=1; i<=N; i++) {
        if (i%3 == 0) {
            cout << 'x';
        } else {
            cout << 'o';
        }
    }
}