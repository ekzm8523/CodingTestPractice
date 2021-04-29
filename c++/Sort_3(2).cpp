//
//
//#include <string>
//#include <vector>
//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//int solution(vector<int> citations) {
//    int h_index = 0;
//    int size = citations.size();
//    sort(citations.begin(),citations.end(),greater<int>());
//
//    for(int i=0;i<size;i++){
//        if(citations[i] <= h_index) break;
//        h_index++;
//    }
//    return h_index;
//}
//
//int main(){
//
//    vector<int> citations = {0,1,1,1,3,3,5};
//    cout << solution(citations);
//    return 0;
//}