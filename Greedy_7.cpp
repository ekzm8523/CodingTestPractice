//
// Created by Macbook Pro on 2020/12/26.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
     int n,m,k;

     cin >> n >> m >> k;

     vector<int> ar(n);
     for(int i=0;i<n;i++)
         cin >> ar[i];

     sort(ar.begin(),ar.end(),greater<int>());
     int first=0,second=0;
     first = ar[0];
     int index=1;
     while(second == 0){
         if(ar[index] != first){
             second = ar[index];
             break;
         }
         index++;
     }

     int answer = 0;
     int cnt=0;
     for(int i=0;i<m;i++){
         if(cnt == k){
             cnt = 0;
             answer += second;
         }else{
            answer += first;
            cnt++;
         }
     }
     cout << answer;
}