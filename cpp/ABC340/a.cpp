#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int A, B, D;
    cin >> A >> B >> D;
    while (A <= B)
    {
        cout << A << " ";
        A += D;
    }
}