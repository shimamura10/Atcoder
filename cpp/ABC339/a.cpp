#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    string S;
    cin >> S;
    string ans;
    for (auto s : S)
    {
        if (s == '.')
        {
            ans = "";
        } else
        {
            ans += s;
        }
    }
    cout << ans;
}