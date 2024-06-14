#include<iostream>
using namespace std;
int main() {
    int N, M;
    cin >> N >> M;
    string S;
    cin >> S;
    int maxLogo = 0, currentNormal = M, currentLogo = 0;
    for (auto s : S) {
        switch (s)
        {
        case '0':
            currentNormal = M;
            currentLogo = maxLogo;
            break;
        case '1':
            if (currentNormal > 0) {
                currentNormal -= 1;
            } else if (currentLogo > 0) {
                currentLogo -= 1;
            } else {
                maxLogo += 1;
            }
            break;
        case '2':
            if (currentLogo > 0) {
                currentLogo -= 1;
            } else {
                maxLogo += 1;
            }
            break;
        default:
            break;
        }
    }
    cout << maxLogo;
}