#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int cmp(const void *a,const void *b)
{
    return *(double *)a - *(double *)b;
}

int qsort_version()
{
    //随机产生10亿个数
    clock_t start,end;
    double Total_time;
    start = clock();
    double *rand_arr;
    rand_arr = (double *)malloc(sizeof(double) * 100000000);
    int i;
    srand((unsigned) time(NULL));
    for(i=0;i<100000000;i++)
    {
        double cur_rand = (double)rand() / RAND_MAX;
        *(rand_arr + i) = cur_rand;
    }
    end = clock();
    Total_time = (double)(end-start)/CLOCKS_PER_SEC;
    printf("%f seconds\n",Total_time);
    start = clock();
    qsort(rand_arr,100000000,sizeof(double),cmp);
    end = clock();
    Total_time = (double)(end-start)/CLOCKS_PER_SEC;
    printf("%f seconds\n",Total_time);
}

int main() {
    qsort_version();
    return 0;
}