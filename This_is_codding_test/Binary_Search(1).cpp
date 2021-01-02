////
//// Created by Macbook Pro on 2020/12/31.
////
//#include <iostream>
//#include <algorithm>
//#include <vector>
//using namespace std;
//
//int N = 4;
//int M = 6;
//int height = 0;
//int cntDduck(vector<int> v, int h){
//    int sum=0;
//    for(int i=v.size()-1;i>=0;i--){
//        if(v[i] > h)
//        sum += v[i]-h;
//    }
//    cout << sum << endl;
//    return sum;
//}
//
//void solution(vector<int> v,int left,int right){
//
//    if(left > right) return;
//
//    int mid = (left+right)/2;
//    int cnt = cntDduck(v,mid);
//    if(cnt >= M) {
//        height = mid;
//        solution(v,mid+1,right);
//    }
//    else if(cnt < M){
//        solution(v,left,mid-1);
//    }
//
//}
//
//int main(){
//
//    vector<int> v = {19,15,10,17};
//    sort(v.begin(),v.end());
//
//    for(int i=0;i<v.size();i++)
//        //cout <<v[i] << " ";
//    solution(v,0,v[v.size()-1]);
//
//
//    cout << height;
//
//
//    return 0;
//}
