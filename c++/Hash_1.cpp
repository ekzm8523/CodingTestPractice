////
//// Created by Macbook Pro on 2020/12/21.
////
//
//#include <iostream>
//
//using namespace std;
//
//int answer = 0;
//
//void fun(int a,int b,int c,int n,int sum){
//    if(sum == n) answer = 1;
//    if(answer == 1 || sum > n) return;
//    fun(a,b,c,n,sum+a);
//    fun(a,b,c,n,sum+b);
//    fun(a,b,c,n,sum+c);
//}
//
//int main(){
////
//    int a,b,c,n;
//    cin >> a >> b >> c >> n;
//
//    fun(a,b,c,n,0);
//    cout << answer;
//
//}