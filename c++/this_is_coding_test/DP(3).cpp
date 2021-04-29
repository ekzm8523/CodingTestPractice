////
//// Created by Macbook Pro on 2021/01/02.
////
//
//#include <iostream>
//#include <vector>
//
//using namespace std;
//
//int main(){
//
//    int n = 100;
//    vector<int> v(n);
//
//    fill(v.begin(),v.end(),0);
//
//    for(int i=2;i<n;i++){
//        v[i] = v[i-1] + 1;
//        if(i % 5 == 0 && v[i] > v[i/5]+1)
//            v[i] = v[i/5]+1;
//        else if(i % 3 == 0 && v[i] > v[i/3]+1)
//            v[i] = v[i/3]+1;
//        else if(i % 2 == 0 && v[i] >v[i/2]+1)
//            v[i] = v[i/2]+1;
//    }
//    for(auto it : v)
//        cout << it << endl;
//
//
//    return 0;
//}
