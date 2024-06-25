#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int> A;
    for (size_t i = 0; i < N; i++)
    {
        int a;
        cin >> a;
        A.emplace_back(a);
    }
    
    long long people = 0;
    long long m = 0;
    for (auto a : A)
    {
        people += a;
        m = min(m,people);
    }
    cout << people - m;
}