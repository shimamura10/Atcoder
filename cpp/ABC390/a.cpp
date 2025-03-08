#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> A(5);
    for (int i=0; i<5; i++) {
        cin >> A[i];
    }

    int cnt = 0;
    for (int i=0; i<4; i++) {
        if (A[i] > A[i+1]) {
            swap(A[i], A[i+1]);
            cnt++;
        }
    }

    if (cnt == 1) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}