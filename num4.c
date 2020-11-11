//#include <stdio.h>
//
//int input(int *p){ // 배열 x의 시작 주소를 인자로 받아 종료 조건까지 정수를 입력받아 배열에 저장하고, 배 열 원소의 개수를 반환한다.
//    int len=0;
//    int *fp;
//
//    for(fp = p;fp < p + 100; fp++){
//        scanf("%d",fp);
//        if(*fp == -1)break;
//        len++;
//    }
//
//    return len;
//
//}
//int *sel_next(int *p){ //배열의 한 원소의 주소 p를 인자로 받아, p가 가리키는 원소부터 원소 값의 증가 또는 감 소가 끝나는 마지막 원소의 주소를 반환 한다.
//                        // 위 예제의 경우, x[4]의 주소가 인자로 전 달되면, x[7]의 주소가 반환된다.
//    int *fp = p+1;
//    int *prev_fp = p;
//    int flag = 0; // 기본 내림차순
//    if(*fp > *prev_fp) flag = 1; // flag == 1  => 오름차순
//    for(fp = p+1; fp < p + 99; fp++){
//        if(*fp == -1) return fp;
//
//        if(flag == 1)
//            if(*fp < *prev_fp) return fp;
//        if(flag == 0)
//            if(*fp > *prev_fp) return fp;
//        prev_fp = fp;
//    }
//    return fp;
//}
//int number(int *p, int *q){ //x[M]의 위치와 sel_next에서 반환된 위치를 인자로 받아, 두 포인터 사이의 한 자리 정수 를 모아, 하나의 정수로 만들어 반환 한다.
//    int result = 0;
//
//    result *= 10;
//    result += *p;
//    p++;
//    while(p != q){
//        result *= 10;
//        result += *p;
//        p++;
//    }
//    return result;
//}
//int main()
//{
//    int ar[100];
//    int *p = ar;
//    int len;
//    int *p2 = p;
//    int *prev_p = p;
//    len = input(p);
//
//    while(*p2 != -1) {
//        prev_p = p2;
//
//        p2 = sel_next(prev_p);
//        printf("%d\n",number(prev_p,p2));
//    }
//    return 0;
//#pragma warning(disable: 4996)
//}


/*
5
1 1 1 1 1
1 1 0 0 1
1 0 0 0 1
0 0 0 0 1
1 1 1 0 0
3 2

5
1 0 0 1 0
0 1 0 0 0
1 1 0 0 0
1 0 1 0 1
1 1 0 0 1

 */
//
//#include <stdio.h>
//#include <string.h>
//int changeInt(char *ar){
//    int sum = 0;
//    int len = strlen(ar);
//    //printf("%d",len);
//    for(int i=0;i<len;i++){
//        if(ar[i] >= 'a' && ar[i] <= 'z') {
//            if (ar[i] - 96 < 10) {
//                sum *= 10;
//                sum += ar[i] - 96;
//            } else {
//                sum *= 100;
//                sum += ar[i] - 96;
//            }
//        }
//        if(sum > 2147483647) return 0;
//    }
//    return sum;
//}
//
//int main()
//{
//    char ar[100];
//    char ar2[100];
//    int i=0;
//    int j=0;
//    int result = 0;
//    gets(ar);
//    for(i=0;i<strlen(ar);i++){
//        ar2[j] = ar[i];
//        if(ar[i] == ' ') {
//            ar2[j] = '\n';
//            result += changeInt(ar2);
//            j = 0;
//            continue;
//        }
//        j++;
//    }
//    result += changeInt(ar2);
//    if(result >= 2147483647) result = -1;
//    printf("%d",result);
//    return 0;
//}