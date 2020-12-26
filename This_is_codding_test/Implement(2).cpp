////
//// Created by Macbook Pro on 2020/12/27.
////
//
//#include <iostream>
//#include <vector>
//#include <String>
//
//using namespace std;
//
//int solution(int x,int y){
//
//    int answer = 0;
//
//    if( x + 1 < 8 && y - 2 >= 0) answer++;
//    if( x + 2 < 8 && y - 1 >= 0) answer++;
//    if( x + 2 < 8 && y + 1 < 8) answer++;
//    if( x + 1 < 8 && y + 2 < 8) answer++;
//    if( x - 1 >= 0 && y + 2 < 8) answer++;
//    if( x - 2 >= 0 && y + 1 < 8) answer++;
//    if( x - 2 >= 0 && y - 1 >= 0) answer++;
//    if( x - 1 >= 0 && y - 2 >= 0) answer++;
//
//    return answer;
//}
//
//int main(){
//
//    int x,y;
//    string st;
//    cin >> st;
//    x = st[1] - '1';
//    y = st[0] - 'a';
//
//
//    cout << solution(x,y);
//
//    return 0;
//}
//