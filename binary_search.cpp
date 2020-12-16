////
//// Created by Macbook Pro on 2020/12/16.
////
//
//#include <iostream>
//
//
//bool Binary_search(int *arr, int len, int key){
//    int start = 0;
//    int end = len-1;
//    int mid;
//
//    while(end - start >= 0){
//        mid = (start + end) / 2;
//
//        if (arr[mid] == key){ // find
//            return true;
//        } else if(arr[mid] > key){ // mid값이 key값보다 크다면
//            end = mid - 1; // end를 mid-1로 변경
//        } else{
//            start = mid + 1; // mid값이 key값보다 작다면 start를 mid + 1로 변경
//        }
//    }
//    return false; // 못찾았다는거임
//}
//bool Recur_binary_search(int *arr, int start, int end, int key){
//    if (start > end) return false;
//    int mid = (start + end ) / 2;
//    if(arr[mid] == key) return true;
//    else if(arr[mid] > key) return Recur_binary_search(arr,start,mid-1,key);
//    else return Recur_binary_search(arr,mid+1,end,key);
//}
//
//using namespace std;
//int main()
//{
//    int n = 100;
//    int arr[n];
//
//    for(int i=0;i<n;i++)
//        arr[i] = i;
//
//    cout << "exist : " << Binary_search(arr,n,90) << endl;
//    cout << "exist : " << Recur_binary_search(arr,0,n-1,90) << endl;
//
//    return 0;
//}