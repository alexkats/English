#include <iostream>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <vector>
#include <ctime>
#include <algorithm>
#include <set>

using namespace std;

vector <string> v;

int main() {
    srand(time(0));

    string s;
    int n = 0;

    while (getline (cin, s)) {
        v.push_back(s);
        n++;
    }

    vector <char> used(n + 1, 0);
    used[n] = 1;
    int q = 0;

    while (q != n) {
        int num = n;

        while (used[num]) {
            num = rand () % n;
        }

        used[num] = 1;
        cout << v[num] << endl;
        q++;
    }

    return 0;
}
