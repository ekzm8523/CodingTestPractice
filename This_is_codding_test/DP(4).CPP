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
//    int n,target;
//    cin >> n >> target;
//    vector<int> v(n); // V(k)
//    vector<int> a(target+1,10001); //
//
//    sort(v.begin(),v.end()); // 오름차순 정렬
//
//    for(int i=0;i<n;i++) {
//        cin >> v[i];
//        a[v[i]] = 1;
//    }
//
//
//
//    for(int i=v[0]+1;i<=target;i++){
//        for(int j=0;j<v.size();j++){
//            int k = v[j];
//            if(i-k > 0 && a[i-k] != 10001)
//                if(a[i-k]+1 < a[i])
//                    a[i] = a[i-k] + 1;
//        }
//    }
//
//
//    for(int i=0;i<=target;i++)
//        cout << " i  = " << i << " a[i] = " << a[i] << endl;
//
//
//
//    return 0;
//}