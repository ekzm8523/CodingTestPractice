/*
// Created by Macbook Pro on 2020/11/11.

*/
#include <queue>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;

    return answer;
}

int main(){
    vector<int> priorities = {4,2,1,3,8,7};
    int location = 3;

    cout << solution(priorities,location) << endl;

}
/*
 *
 * int maxPriorities(queue<int> priorities){
    int max = 0;
    int size = priorities.size();
    for(int i=0;i<size;i++) {
        if( max < priorities.front()) max = priorities.front();
        priorities.pop();
    }
    return max;
}
int solution(vector<int> priorities, int location) {
    int answer = 0;
    int index=0;
    int size = priorities.size();

    queue<int> waitQueue;

    for(auto it: priorities)
        waitQueue.push(it);

    while(waitQueue.size() > 0){
        if(priorities[index] == 0){
            index++;
            if(index == size) index = 0;
            continue;
        }

        if(waitQueue.front() == maxPriorities(waitQueue)){
            waitQueue.pop();
            answer++;
            priorities[index] = 0;
            if(location == index) return answer;
        }
        else {
            waitQueue.push(waitQueue.front());
            waitQueue.pop();
        }
        index++;
        if(index == size) index = 0;
    }
    return answer;
}

 */