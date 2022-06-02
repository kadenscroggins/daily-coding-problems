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


    return 0;
}

template<typename T>
class Node {
public:
    void add(T data) {
        this->data = data;
    }
private:
    T data;
};