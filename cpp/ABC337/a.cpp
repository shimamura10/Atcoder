# include <iostream>
using namespace std;
int main ()
{
    int N;
    cin >> N;
    int tPoint=0, aPoint=0;
    for (auto i=0; i<N; i++)
    {
        int x,y;
        cin >> x >> y;
        tPoint += x;
        aPoint += y;
    }
    
    if (tPoint > aPoint)
    {
        cout << "Takahashi";
    } else if (tPoint < aPoint)
    {
        cout << "Aoki";
    } else
    {
        cout << "Draw";
    }
    return 0;
}