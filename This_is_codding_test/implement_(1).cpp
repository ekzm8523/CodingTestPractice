////
//// Created by Macbook Pro on 2020/12/27.
////
//#include <iostream>
//#include <vector>
//#include <unordered_map>
//#include <set>
//using namespace std;
//
//int main(){
//
//    int N;
//    unordered_map<char,int> map;
//    cin >> N;
//
//    int p_x = 0, p_y = 0;
//
//    vector<int> X = {-1,0,1,0};     // 시계방향
//    vector<int> Y = {0,1,0,-1};
//
//    map['U'] = 0;
//    map['R'] = 1;
//    map['D'] = 2;
//    map['L'] = 3;
//
//    char c = 'R';
//
//    while(c != '0'){
//        cin >> c;
//        int i = map[c];
//        if(p_x + X[i] >= 0 && p_x + X[i] < N)
//            p_x += X[i];
//        if(p_y + Y[i] >= 0 && p_y + Y[i] < N)
//            p_y += Y[i];
//        cout << p_x << " " << p_y << endl;
//
//    }
//
//    cout << p_x << " " << p_y << endl;
//
//
//
//
//    return 0;
//}
