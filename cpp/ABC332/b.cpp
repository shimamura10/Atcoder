# include<iostream>
using namespace std;
int main () {
    int K, G, M;
    cin >> K >> G >> M;
    auto currentG = 0, currentM = 0;
    for (int i = 0; i < K; i++)
    {
        if (currentG == G) {
            currentG = 0;
        } else if (currentM == 0) {
            currentM = M;
        } else {
            if (currentM < G - currentG) {
                currentG += currentM;
                currentM = 0;
            } else {
                currentM -= G - currentG;
                currentG = G;
            }
        }
    }
    cout << currentG << " " << currentM;
}