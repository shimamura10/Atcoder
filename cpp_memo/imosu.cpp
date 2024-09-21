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

// 1次元いもす法
struct Line
{
    vector<int> A;
    Line(int N) : A(N, 0) {}
    void add(int l, int r){
        A[l]++;
        A[r]--;
    }
    void build(){
        for (int i = 1; i < A.size(); i++){
            A[i] += A[i-1];
        }
    }
};

// 2次元いもす法
struct Square
{
    vector<vector<int>> A;
    Square(int N) : A(N, vector<int>(N, 0)) {}
    void add(int lx, int ly, int rx, int ry){
        A[lx][ly]++;
        A[rx][ry]++;
        A[lx][ry]--;
        A[rx][ly]--;
    }
    void build(){
        for (int i = 1; i < A.size(); i++){
            for (int j = 0; j < A.size(); j++){
                A[i][j] += A[i-1][j];
            }
        }
        for (int i = 0; i < A.size(); i++){
            for (int j = 1; j < A.size(); j++){
                A[i][j] += A[i][j-1];
            }
        }
    }
};

int main(){
    cout << "1次元いもす法" << endl;
    vector<vector<int>> l = {{0, 3}, {1, 4}};
    Line line(5);
    for (auto x : l){
        line.add(x[0], x[1]);
    }
    line.build();
    for (int i = 0; i < 5; i++){
        cout << line.A[i] << " ";
    }
    cout << endl;

    cout << "2次元いもす法" << endl;
    vector<vector<int>> s = {{0, 0, 3, 3}, {1, 1, 4, 4}};
    Square square(5);
    for (auto x : s){
        square.add(x[0], x[1], x[2], x[3]);
    }
    square.build();
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            cout << square.A[i][j] << " ";
        }
        cout << endl;
    }
}