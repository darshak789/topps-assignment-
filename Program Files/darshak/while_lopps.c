#include<stdio.h>
int main()
{
    int num,i;
    printf("enter your number");
    scanf("%d",&num);
    i=1;
    while ( i<=10 )
    {
       printf("%d X %d =%d\n",num,i,num*i);
       i++;

    }
    return 0; 
}
    


