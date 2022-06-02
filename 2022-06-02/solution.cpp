#include <iostream>
#include <bitset>

using namespace std;

int main() {
    /* Testing XORing characters.
    unsigned char a = 195;
    unsigned char b = 87;
    unsigned char c;
    c= a ^ b; // XOR

    cout << bitset<8>(a) << endl;
    cout << bitset<8>(b) << endl;
    cout << bitset<8>(c) << endl;
    */
   List<int> *list = new List<int>();

    cout << "End of program" << endl;
    return 0;
}

template<typename T>
class List {
public:
    void add(T data) {
        uintptr_t previous;
        uintptr_t current;
        uintptr_t next;


    }
    T get(int index) {
        return new T;
    }
private:
    struct Node {
        T data;
        uintptr_t pointer;
    };
    Node *head;
};