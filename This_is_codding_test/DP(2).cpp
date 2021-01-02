////
//// Created by Macbook Pro on 2021/01/01.
////
//
//
//#include <iostream>
//#include <vector>
//
//using namespace std;
//
//int main(){
//    int n = 100;
//    vector<int> v = {1,3,1,5,2,4,4,3,2,1,5};
//    vector<int> v2(n);
//
//    v2[0] = v[0];
//    v2[1] = v[0]>v[1]?v[0]:v[1];
//
//    for(int i=2;i<n;i++){
//        v2[i] = v2[i-1]>(v2[i-2]+v[i])?v2[i-1]:v2[i-2]+v[i];
//    }
//    for(auto it : v2)
//        cout << it << endl;
//
//
//
//
//    return 0;
//}