////
//// Created by Macbook Pro on 2020/11/15.
////
///*
//수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
//
//1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
//2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
//3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
//
//1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
//
//제한 조건
//시험은 최대 10,000 문제로 구성되어있습니다.
//문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
//가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
//입출력 예
//answers	    return
//[1,2,3,4,5]	[1]
//[1,3,2,4,2]	[1,2,3]
//입출력 예 설명
//입출력 예 #1
//
//수포자 1은 모든 문제를 맞혔습니다.
//수포자 2는 모든 문제를 틀렸습니다.
//수포자 3은 모든 문제를 틀렸습니다.
//따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.
//
//입출력 예 #2
//
//모든 사람이 2문제씩을 맞췄습니다.
// */
//#include <string>
//#include <vector>
//#include <iostream>
//
//using namespace std;
//
//vector<int> solution(vector<int> answers) {
//    vector<int> answer;
//    vector<int> stu_1 = {1,2,3,4,5,0};
//    vector<int> stu_2 = {2,1,2,3,2,4,2,5,0};
//    vector<int> stu_3 = {3,3,1,1,2,2,4,4,5,5,0};
//    int index1=0,index2=0,index3=0;
//    for(int i=0;i<answers.size();i++,index1++,index2++,index3++){
//        if(index1 == 5) index1 = 0;
//        if(index2 == 8) index2 = 0;
//        if(index3 == 10) index3 = 0;
//
//        if(answers[i] == stu_1[index1]) stu_1[5]++;
//        if(answers[i] == stu_2[index2]) stu_2[8]++;
//        if(answers[i] == stu_3[index3]) stu_3[10]++;
//    }
//
//    int max=0;
//
//    if(max < stu_1[5]) max = stu_1[5];
//    if(max < stu_2[8]) max = stu_2[8];
//    if(max < stu_3[10]) max = stu_3[10];
//
//    if(max == stu_1[5]) answer.push_back(1);
//    if(max == stu_2[8]) answer.push_back(2);
//    if(max == stu_3[10]) answer.push_back(3);
//    return answer;
//}
//
//int main(){
//
//    vector<int> answers ={1,2,3,4,5};
//    //vector<int> answers ={1,3,2,4,2};
//
//    answers = solution(answers);
//    for(auto it:answers)
//        cout << it << " ";
//    cout << endl;
//
//    return 0;
//}
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
