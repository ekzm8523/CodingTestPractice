////
//// Created by Macbook Pro on 2020/12/21.
////
//#include <iostream>
//using namespace std;
//int N,K;
//int arr[5];
//int choice[5];
//int cnt;
//
//void comb(int number, int idx){
//    // 선택한 원소의 갯수가 K(선택할 원소의 갯수)보다 크면
//    // 선택한 원소 출력 & 함수 끝내기
//    if(idx >= K){
//        for (int i=0;i<K;i++)
//            cout << choice[i] << " ";
//        cout << endl;
//        return;
//    }
//    // 집합의 원소의 갯수보다, 오버되게 탐색하면 종료 (실패)
//    if(number >= N)
//        return;
//
//    // 선택한 원소 선택 배열에 저장
//    choice[idx] = arr[number];
//    // 1. 선택 후 다음, 2. 미선택 후 다음
//    comb(number + 1,idx + 1);
//    comb( number + 1, idx);
//}
//
//int main(){
//
//    cin >> N >> K;
//
//    for(int i=0;i<N;i++)
//        cin >> arr[i];
//    comb(0,0);
//
//    return 0;
//}
