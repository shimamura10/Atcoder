#include <iostream>
#include <vector>
using namespace std;

class Sample
{
private:
    int _a;
public:
    Sample(int a);
    Sample(const Sample& sample);
    Sample(Sample&& rhs);
    ~Sample();
};

Sample::Sample(int a) : _a(a)
{
    cout << "コンストラクタが呼ばれました" << endl;
}

Sample::Sample(const Sample& sample) {
    cout << "コピーコンストラクタが呼ばれました" << endl;
    _a = sample._a;
}

Sample::Sample(Sample&& rhs) {
    cout << "ムーブコンストラクタが呼ばれました" << endl;
    _a = move(rhs._a);
};

Sample::~Sample()
{
    cout << "デストラクタが呼ばれました" << endl;
}


int main(int argc, char const *argv[])
{
    vector<Sample> v;
    cout << "push_back" << endl;
    v.push_back(0);
    // cout << "push_back(Sample(0))" << endl;
    // v.push_back(Sample(0));
    cout << "emplace_back" << endl;
    v.emplace_back(0);
    cout << "wrong emplace_back" << endl;
    v.emplace_back(Sample(0));
    return 0;
}
