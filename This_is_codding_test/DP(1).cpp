//////
////// Created by Macbook Pro on 2021/01/01.
//////
//
//#include <iostream>
//#include <vector>
//
//using namespace std;
//
//long long fiboRecur(vector<long long> &v, int index){
//
//    cout << "f(" << index << ") : " << v[index] << endl;
//
//    if(index == 1 || index == 2)
//        return 1;
//    if(v[index] != 0) return v[index];
//
//    v[index] = fiboRecur(v,index-1) + fiboRecur(v,index-2);
//    return v[index];
//}
//
//
//long long fibo(vector<long long> v, int index){
//
//    v[0] = 1;
//    v[1] = 1;
//    for(int i=2;i<index;i++){
//        v[i] = v[i-1] + v[i-2];
//    }
//    return v[index-1];
//}
//
//int main(){
//    vector<long long > v(100);
//
//    cout << fiboRecur(v,8) << endl;
//    cout << fibo(v,8);
//
//}
