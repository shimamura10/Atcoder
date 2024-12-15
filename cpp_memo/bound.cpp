#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4, 5};
    auto lower_iter = lower_bound(v.begin(), v.end(), 3);
    auto upper_iter = upper_bound(v.begin(), v.end(), 3);
    cout << *lower_iter << endl;
    cout << *upper_iter << endl;
}