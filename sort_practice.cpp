////
//// Created by Macbook Pro on 2020/12/22.
////
//#include <iostream>
//#include <vector>
//using namespace std;
//
//void qsort(vector<int>& v,int s,int e){
//    int pivot = v[s];
//    int bs = s, be = e;
//    while(s<e){
//        while(pivot<=v[e]&&s<e)e--;
//        if(s>e)break;
//        while(pivot>=v[s]&&s<e)s++;
//        if(s>e)break;
//        swap(v[s],v[e]);
//    }
//    swap(v[bs],v[s]);
//    if(bs<s)
//        qsort(v,bs,s-1);
//    if(be>e)
//        qsort(v,s+1,be);
//}
//
//
//int main(){
//
//    vector<int> ar = {9,8,7,6,5,4,3,2,1};
//
//    for(int i=0;i<ar.size()-1;i++){ // 선택 정렬
//        for(int j=i+1;j<ar.size();j++){
//            if(ar[i] > ar[j]){
//                swap(ar[i],ar[j]);
//
//            }
//        }
//    }
//
//    ar = {9,8,7,6,5,4,3,2,1};
//    for(int i=1;i<ar.size();i++){ // 삽입 정렬
//        int key = ar[i];
//        for(int j=i-1;j>=0;j--){
//            if(key > ar[j]) break;
//            if(key < ar[j]) swap(ar[j],ar[j+1]);
//        }
//    }
//
//    ar = {9,8,7,6,5,4,3,2,1};
//    for(int i=0;i<ar.size()-1;i++){ // 버블 정렬
//        for(int j=1;j<ar.size()-i;j++){
//            if(ar[j-1] < ar[j]) swap(ar[j-1],ar[j]);
//        }
//    }
//
//    ar = {9,8,7,6,5,4,3,2,1};
//    qsort(ar,0,ar.size()-1);
//
//
//    for(auto it : ar)
//        cout << it << " ";
//    cout << endl;
//    return 0;
//}
