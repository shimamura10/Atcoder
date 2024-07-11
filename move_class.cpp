#include <iostream>
#include <vector>
using namespace std;

template <class T>
class clone_ptr
{
    private:
    //コピー可能／ムーブ可能であることを示す
    BOOST_COPYABLE_AND_MOVABLE(clone_ptr);

    T* ptr;

    public:
    //コンストラクタ
    explicit clone_ptr(T* p = 0) : ptr(p) {cout << "コンストラクタ" << endl;}

    //コンストラクタ
    ~clone_ptr() { delete ptr; cout << "デストラクタ" << endl;}

    //コピーセマンティクス

    //コピーコンストラクタ(クラスの型のconst参照を引数にとる)
    clone_ptr(const clone_ptr& p)
        : ptr(p.ptr ? p.ptr->clone() : 0) { cout << "コピーコンストラクタ" << endl;}

    // コピー代入演算子(BOOST_COPY_ASSIGN_REF(クラス名)を引数に取る)
    clone_ptr& operator=(BOOST_COPY_ASSIGN_REF(clone_ptr) p)
    {
        if (this != &p){
            T *tmp_p = p.ptr ? p.ptr->clone() : 0;
            delete ptr;
            ptr = tmp_p;
        }
        return *this;
    }

    //ムーブセマンティクス

    //ムーブコンストラクタ(BOOST_RV_REF(クラス名)を引数に取る)
    clone_ptr(BOOST_RV_REF(clone_ptr) p)
        : ptr(p.ptr) { p.ptr = 0; cout << "ムーブコンストラクタ" << endl;}

    //ムーブ代入演算子(BOOST_RV_REF(クラス名)を引数に取る)
    clone_ptr& operator=(BOOST_RV_REF(clone_ptr) p)
    {
        if (this != &p){
            delete ptr;
            ptr = p.ptr;
            p.ptr = 0;
        }
        return *this;
    }
};

int main(int argc, char const *argv[])
{
    vector<clone_ptr<int>> v;
    cout << "push_back" << endl;
    int* a{0};
    v.push_back(clone_ptr<int>());
    cout << "emplace_back" << endl;
    v.emplace_back();
    cout << "wrong emplace_back" << endl;
    v.emplace_back(clone_ptr<int>());
    return 0;
}