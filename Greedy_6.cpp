////
//// Created by Macbook Pro on 2020/11/19.
////
//
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> node;
bool cmp(vector<int> a, vector<int> b){
    return a[0]>b[0];
}

int solution(vector<vector<int>> routes) {
    int answer = 0, flag = 30001;
    sort(routes.begin(),routes.end(),cmp);

    for(int i=0;i<routes.size();i++){
        if(flag > routes[i][1]){
            flag = routes[i][0];
            answer++;
        }
    }

    return answer;
}

int main(){
    vector<vector<int>> routes = {{-20,15},{-14,-5},{-18,-13},{-5,-3}};
    cout << solution(routes);

    return 0;
}