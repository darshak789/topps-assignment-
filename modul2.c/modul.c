#include<stdio.h>
void main()
{

int a,b;

printf("enter your number 1:");
scanf("%d",&a);
printf("enter your number 2:");
scanf("%d",&b);
int add = a + b;
int sub = a - b;
int mul = a * b;
float div = a / b;
int mod = a % b;
printf("addtion=%d\nsubtraction=%d\nmultiplication=%d\ndivison=%.2f\nmodulus=%d\n",add,sub,mul,div,mod);


}

