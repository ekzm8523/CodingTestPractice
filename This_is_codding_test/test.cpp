//
// Created by Macbook Pro on 2021/01/05.
//


#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>
using namespace std;

int main(){

    bitset<10> bit;
    bit.set(1);
    bit = 10;
    cout << bit << endl;
    cout << bit.flip(2);

    return 0;
}
