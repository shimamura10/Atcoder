#include<bits/stdc++.h>
using namespace std;

int main() {
    cout << !-1 << endl;
    cout << !0 << endl;
    cout << !1 << endl;
    vector<int> A = {1, 2};
    vector<string> B = {"a", "b", "c"};
    for (const auto& [a, b] : std::views::cartesian_product(A, B)) {
        cout << "(" << a << ", " << b << ") ";
    }
    cout << endl;

    vector<int> C = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    for (const auto& c : C | views::reverse | views::take(5)) {
        cout << c << " ";
    }

    vector<int> v(0);
    cout << v.size() << endl;

    int a = 3;
    int c = 9;
    long long b = 1e11;
    cout << a * b << endl;
}