#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string S;
    cin >> S;
    string sortedS = S;
    std::sort(sortedS.begin(), sortedS.end());
    if (S == sortedS)
    {
        cout << "Yes";
    } else
    {
        cout << "No";
    }
}