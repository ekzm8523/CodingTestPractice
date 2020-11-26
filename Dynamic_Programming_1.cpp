//
// Created by Macbook Pro on 2020/11/25.
//
/*
 * 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5
5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
입출력 예
N	number	return
5	12	    4
2	11	    3
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.
 */


#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <math.h>
using namespace std;

int get_basic_number(int N, int cnt) {
    int res = 0;

    while (cnt > 0) {
        cnt -= 1;
        res += N * pow(10, cnt);
    }

    return res;
}

int solution(int N, int number) {
    int answer = -1;

    const int MIN = 8;

    vector<set<int>> s(MIN);

    int idx = 1;

    for (int i=0; i< s.size(); i++){
        s[i].insert(get_basic_number(N, idx));
        idx += 1;
    }
    for (int i=0; i< s.size(); i++){
        for( auto it : s[i])
            cout << it << " ";
        cout << endl;
    }

    for (int i = 1; i < MIN; i++) {
        for (int j = 0; j < i; j++) {
            for (const auto & op1 : s[j]) {
                for (const auto & op2 : s[i - j - 1]) {
                    s[i].insert(op1 + op2);
                    s[i].insert(op1 - op2);
                    s[i].insert(op1 * op2);

                    if (op2 != 0)
                        s[i].insert(op1 / op2);
                }
            }
        }
        if (s[i].find(number) != s[i].end()) {
            answer = i + 1;
            break;
        }
    }
    return answer;
}

int main() {
    int N, number, result;

    result = solution(5, 11);
    cout << result;
}