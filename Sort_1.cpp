//
// Created by Macbook Pro on 2020/11/13.
//

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for(int i=0;i<commands.size();i++){
        vector<int> sortArray;
        for(int j=commands[i][0]-1;j<commands[i][1];j++)
            sortArray.push_back(array[j]);
        sort(sortArray.begin(),sortArray.end());
        answer.push_back(sortArray[commands[i][2]-1]);
    }
    return answer;
}

int main(){
    vector<int> array = {1,5,2,6,3,7,4};
    vector<vector<int>> commands = {{2,5,3},{4,4,1},{1,7,3}};
    vector<int> answer = solution(array,commands);

    for(auto it:answer)
        cout << it << " ";
    cout << endl;
    return 0;
}

