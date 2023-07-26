//Write a program in C to swap 2 integer variable without using 3rd variable
//LLONG_MAX=9,223,372,036,854,775,807
#include<stdio.h>
#include<time.h>

void swap(long long int *a, long long int *b)           
{
    *a=*a+*b-(*b=*a);
}

int main()
{
    clock_t start,end;
    long long int num1=9223372036854775807,num2=9223372036854775806;

    start=clock();
    swap(&num1,&num2);                         
    printf("The numbers after swapping-- \n");
    printf("%lld\n%lld\n",num1,num2);
    end=clock();

    double duration = ((double)end - start)/CLOCKS_PER_SEC;
    printf("Time taken to execute in seconds : %lf\n", duration);
    /*Output--
    The numbers after swapping-- 
    9223372036854775806
    9223372036854775807
    Time taken to execute in seconds : 0.002000*/
    return 0;
}