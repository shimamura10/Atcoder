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
    vector<string> A;
    for (int i=0; i<N; ++i){
        string c;
        cin >> c;
        A.push_back(c);
    }
    vector<string> B;
    for (int i=0; i<N; ++i){
        string c;
        cin >> c;
        B.push_back(c);
    }
    for (int i=0; i<N; ++i){
        for (int j=0; j<N; ++j){
            if (A[i][j] != B[i][j]){
                cout << i+1 << " " << j+1 << endl;
                return 0;
            }
        }
    }
}