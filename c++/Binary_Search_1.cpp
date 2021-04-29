////
//// Created by Macbook Pro on 2020/12/16.
////
//
//#include <iostream>
//#include <vector>
//
//using namespace std;
//long long solution(int n, vector<int> times) {
//    long long answer = 0;
//    sort(times.begin(),times.end());
//    long long  mid,sum,start = 1,end = times[times.size()-1] * (long long)n;
//
//    while(start <= end){
//        sum = 0;
//        mid = (start + end)/2;
//        cout << "start = " << start << " mid = " << mid << " end = " << end << endl;
//
//        for(auto it : times) {
//            sum += (mid / it);
//        }
//        cout << sum << endl;
//        if ( sum >= n ){
//            answer = mid;
//            end = mid - 1;
//        }
//        else if( sum < n ) start = mid + 1;
//
//    }
//    return answer;
//}
//int main()
//{
//    int n = 6;
//    vector<int> times ={7,10,100};
//
//    cout << solution(n,times) << endl;
//
//    return 0;
//}