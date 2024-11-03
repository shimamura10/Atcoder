#include <iostream>

class Memory {
    int id;
    int id2;

public:
    // コンストラクタ
    Memory(int id) : id(id), id2(id*10) {
        std::cout << "Memory " << id << " is created at " << this << "." << std::endl;
    }

    // デストラクタ
    ~Memory() {
        std::cout << "Memory " << id << " is destroyed at " << this << "." << std::endl;
    }

    // コピーコンストラクタ
    Memory(const Memory& other) : id(other.id) {
        std::cout << "Memory " << id << " is copied from " << &other << " to " << this << "." << std::endl;
    }

    // ムーブコンストラクタ
    Memory(Memory&& other) noexcept : id(other.id) {
        other.id = 0; // ムーブ後のオブジェクトを無効な状態にする
        std::cout << "Memory " << id << " is moved from " << &other << " to " << this << "." << std::endl;
    }

    // コピー代入演算子
    Memory& operator=(const Memory& other) {
        if (this != &other) {
            id = other.id;
            std::cout << "Memory " << id << " is copy-assigned from " << &other << " to " << this << "." << std::endl;
        }
        return *this;
    }

    // ムーブ代入演算子
    Memory& operator=(Memory&& other) noexcept {
        if (this != &other) {
            id = other.id;
            other.id = 0; // ムーブ後のオブジェクトを無効な状態にする
            std::cout << "Memory " << id << " is move-assigned from " << &other << " to " << this << "." << std::endl;
        }
        return *this;
    }

    void print() {
        std::cout << "Memory " << id << " is at " << this << "." << std::endl;
    }

    void printIdsPointer() {
        std::cout << "Memory's id is " << id << " is at " << &id << ", id2 " << id2 << " is at " << &id2 << std::endl;
    }
};

Memory createMemory(int id) {
    Memory memory(id);
    memory.print();
    return memory;
}

int main() {
    Memory memory1(1);
    Memory memory2(2);
    Memory memory3(3);

    Memory memory4 = memory1; // コピーコンストラクタ
    Memory memory5 = std::move(memory2); // ムーブコンストラクタ
    memory5.print();
    memory1.printIdsPointer();
    memory4.printIdsPointer();
    memory2.printIdsPointer();
    memory5.printIdsPointer();

    auto memory6 = createMemory(4); // ムーブコンストラクタ

    memory3 = memory1; // コピー代入演算子
    memory3 = std::move(memory5); // ムーブ代入演算子


    return 0;
}