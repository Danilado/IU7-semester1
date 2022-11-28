#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
    ofstream out;
    out.open("./a.txt");
    
    for (ll i = 0; i < 100000000; ++i)
        out << to_string(i) << '\n';
    
    return 0;
}
