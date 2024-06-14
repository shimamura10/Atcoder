#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;

int main(){
    long long N;
    cin >> N;
    long long odd=0, even=0, oddNum=0, evenNum=0;
    if (N%2==0)
    {
        even++;
        evenNum = N;
    } else
    {
        odd++;
        oddNum = N;
    }
    long long cost = 0;
    while (oddNum > 1 || evenNum > 1)
    {
        if (oddNum <= 1)
        {
            oddNum = 0;
            odd = 0;
        } 
        cost += evenNum*even + oddNum*odd;
        long long newOdd=0, newEven=0, newOddNum=0, newEvenNum=0;
        if (evenNum/2%2 == 1)
        {
            newOdd = even*2;
            newOddNum = evenNum/2;
        } else
        {
            newEven = even*2;
            newEvenNum = evenNum/2;
        }
        if (newOddNum == 0)
        {
            if (oddNum/2%2 == 1)
            {
                newOddNum = oddNum/2;
            } 
            if ((oddNum+1)/2%2 == 1)
            {
                newOddNum = (oddNum+1)/2;
            }
        }
        if (newEvenNum == 0)
        {
            if (oddNum/2%2 == 0)
            {
                newEvenNum = oddNum/2;
            }
            if ((oddNum+1)/2%2 == 0)
            {
                newEvenNum = (oddNum+1)/2;
            }
        }
        newOdd += odd;
        newEven += odd;

        odd = newOdd;
        even = newEven;
        oddNum = newOddNum;
        evenNum = newEvenNum;
    }
    cout << cost;
}