#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    bool exists = false;

    for (int i = a; i <= b; i++) {
        if (i % c == 0) {
            exists = true;
            break;
        }
    }

    if (exists)
        cout << "NO";
    else
        cout << "YES";

    return 0;
}