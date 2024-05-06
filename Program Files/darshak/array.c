#include<stdio.h>
int main()
{

int a[10],sum=0;
for (int i = 0; i < 10; i++)
{
    printf("enter number: ");
    scanf("%d",&a[i]);
}
for(int i=0; i<10; i++)
   {
     if(a[i] %2 == 0)
      {      
           printf("%d is evan",a[i]);
      }
     else
      {
            printf("%d is odd",a[i]);
      }
  
   }

return 0;


}