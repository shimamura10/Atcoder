#include <iostream>
#include <memory>

int main() {
    std::unique_ptr<int> x(new int(100));
    std::unique_ptr<int> y(std::move(x)); // ムーブは出来るため、所有権の移動は可能。
                                          // 所有権を移動したため、x は何も所有していない。

    std::cout << *y << std::endl;

    return 0;
} // y が所有しているリソースが解放される。