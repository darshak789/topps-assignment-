#include <stdio.h>
int main()
{

    int num, factorial;
    printf("enter the num:");
    scanf("%d", &num);
    for (int i = 1; i <= num; i++)
    {
        factorial = factorial * i;
    }
    printf("factorial=%d", factorial);
    
}