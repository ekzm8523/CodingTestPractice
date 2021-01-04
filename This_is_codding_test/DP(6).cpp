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
//    int n;
//    cin >> n;
//    vector<int> v(n);
//    vector<int> v1(n,1);
//    for(int i=0;i<n;i++)
//        cin >> v[i];
//    reverse(v.begin(),v.end());
//
//
//    for(int i=1;i<n;i++){
//        for(int j=0;j<i;j++){
//            if(v[j] < v[i] && v1[i]<v1[j]+1)
//                v1[i] = v1[j]+1;
//        }
//    }
//    int answer =0;
//    for(auto it : v1)
//        answer = answer>it?answer:it;
//    cout << answer;
//    return 0;
//}