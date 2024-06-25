#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int H, W, N;
    cin >> H >> W >> N;
    vector<string> grid(H, string(W, '.'));
    int h = 0, w = 0;
    int directions[4][2] = {{-1,0}, {0,1}, {1,0}, {0,-1}};
    int d = 0;
    for (size_t i = 0; i < N; i++)
    {
        if (grid[h][w] == '.')
        {
            grid[h][w] = '#';
            d = (d+1)%4;
        } else if (grid[h][w] == '#')
        {
            grid[h][w] = '.';
            d = (d-1+4)%4;
        }
        h = (h+directions[d][0]+H)%H;
        w = (w+directions[d][1]+W)%W;
    }
    
    for (auto a : grid)
    {
        cout << a << endl;
    }
}