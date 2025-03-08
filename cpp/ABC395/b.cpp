#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<char>> A(N, vector<char>(N));
    for (int i=0; i<N; i++) {
        auto j = N - 1 - i;
        if (i <= j) {
            char c = (i%2 == 0) ? '#' : '.';
            for (int k=i; k<=j; k++) {
                A[k][i] = c;
                A[k][j] = c;
                A[i][k] = c;
                A[j][k] = c;
            }
        }
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cout << A[i][j];
        }
        cout << endl;
    }
}