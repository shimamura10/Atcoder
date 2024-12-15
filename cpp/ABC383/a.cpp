#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int water = 0;
    int pret = 0;
    for (int i = 0; i < N; i++) {
        int t, v;
        cin >> t >> v;
        water = max(0, water - (t - pret));
        water += v;
        pret = t;
    }
    cout << water << endl;
}