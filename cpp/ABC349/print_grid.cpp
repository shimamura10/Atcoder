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
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

void print_grid(int a[3][3]) {
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    a[1][1] += 100;
}

int main(){
    int a[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
    print_grid(a);
    cout << "-------------" << endl;
    print_grid(a);
}