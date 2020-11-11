//#include <stdio.h>
//
//void input(int *p, int M){
//    int *fp;
//
//    for(fp = p;fp<p+M;fp++)
//        scanf("%d",fp);
//
//}
//int* sel_max(int *p, int M){
//    int *fp,*fp2;
//    int max=0;
//    int *p_max;
//    int cnt=0;
//
//    for(fp = p;fp<p+M;fp++){
//        cnt=0;
//        for(fp2 = p; fp2<p+M;fp2++) {
//            if(*fp2 == *fp){
//                cnt++;
//            }
//
//
//        }
//        if (max < cnt) {
//            max = cnt;
//            p_max = fp;
//            printf("fp == %d fp2 == %d max == %d cnt == %d\n",*fp,*fp2,max,cnt);
//        }
//    }
//
//    return p_max;
//}
//
//void output(int *p, int N){
//    int *fp;
//
//    for(fp = p;fp<p+N;fp++)
//        printf(" %d",*fp);
//
//}
//
//
//
//int main()
//{
//    int in[100],out[100],*max,i,N,M;
//
//    scanf("%d %d",&N,&M);
//    for(i=0;i<N;i++){
//        input(in,M);
//        max = sel_max(in,M);
//        out[i] = *max;
//    }
//    output(out,N);
//    return 0;
//
//}
//
