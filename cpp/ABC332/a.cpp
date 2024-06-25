#include<iostream>
using namespace std;

int main() {
    int N,S,K;
    cin >> N >> S >> K;
    auto price = 0;
    for (auto i = 0; i < N; i++)
    {
        int p,q;
        cin >> p >> q;
        price += p * q;
    }
    if (price < S) {
        price += K;
    }
    cout << price;
    return 0;
}