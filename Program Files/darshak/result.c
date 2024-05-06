#include<stdio.h>
void main()
{
   int phy,eng,hindi,math,che,total;
   float per;
   printf("enter the 5 subject marks:");
   scanf("%d%d%d%d%d",&phy,&eng,&hindi,&math,&che);

   marks1=int("enter the first subject marks")
   marks2=int("enter the second subject marks")
   marks3=int("enter the third subject marks")
   marks4=int("enter the forth subject marks")
   marks5=int("enter the fifth subject marks")
   printf("enter the 5 subject marks:")
   total=phy+eng+hindi+math+che;
   per=total/500*100

   int marks;
   printf("enter your marks:");
   scanf("%d",&marks);

   if (marks<33 && marks>0)
   {
    printf("fail");
   }
   
   else if (marks<33 && marks>66)
   {
    printf("c");
   }

  else if (marks>60 && marks<85)
   {
    printf("b");
   }

  else if (marks>85 && marks<95)
   {
     printf("a");
   }

  else if (marks>95 && marks<100)
   {
       printf("a+");
   }



    return 0;

}