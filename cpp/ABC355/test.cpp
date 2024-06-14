#include <iostream>
#include <queue>

int main()
{
  // 昇順に処理する
  {
    std::priority_queue<
      int,                // 要素の型はint
      std::vector<int>,   // 内部コンテナはstd::vector (デフォルトのまま)
      std::greater<int>   // 昇順 (デフォルトはstd::less<T>)
    > que;

    que.push(3);
    que.push(1);
    que.push(4);

    while (!que.empty()) {
      std::cout << que.top() << std::endl;
      que.pop();
    }
  }
  std::cout << std::endl;

  // 処理順を表す比較関数オブジェクトにラムダ式を使用する
  {
    auto compare = [](int a, int b) {
      return a < b;
    };

    std::priority_queue<
      int,
      std::vector<int>,
      decltype(compare) // 比較関数オブジェクトを指定
    > que {compare};

    que.push(3);
    que.push(1);
    que.push(4);

    std::cout << que.top();

    while (!que.empty()) {
      std::cout << que.top() << std::endl;
      que.pop();
    }
  }
}