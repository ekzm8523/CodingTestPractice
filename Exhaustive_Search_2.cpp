//
// Created by Macbook Pro on 2020/11/15.
//

/*문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	    3
"011"	    2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
 */

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
bool check(int n){
    if (n < 2) return false;
    for(int i=2;i<n;i++){
        if( n % i == 0) return false;
    }
    return true;
}
int solution(string numbers) {
    vector<int> v;
    int answer = 0;
    vector<int> ans;
    for(auto it:numbers)
        v.push_back(it-'0');
    sort(v.begin(),v.end());

    do{
        for(int i=1;i<=v.size();i++){
            int tmp = 0;
            for( int j=0;j<i;j++){
                tmp = (tmp * 10) + v[j];
                ans.push_back(tmp);
            }
        }
    }while(next_permutation(v.begin(),v.end()));

    sort(ans.begin(),ans.end());
    ans.erase(unique(ans.begin(),ans.end()),ans.end());
    for(auto it:ans){
        if(check(it)){
            answer++;
        }
    }
    return answer;
}
int main(){

    string numbers="17";
    //string numbers="011";

    cout << solution(numbers) << endl;


    return 0;
}
