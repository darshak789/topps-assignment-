#include<stdio.h>
void main()
{
int  age;
printf("enter age:");
scanf("%d",&age);
if(age<18 && age>0)
{
    printf("child");
}

else if  (age>18 && age<40)

{
    printf("young");
}

 else if (age>40 && age<60)

{
    printf("mid young");
}

else if (age>60 && age<100)

{
    printf("senior citzen");
}

 else if  (age>100)

{
    printf("amar");
}

return 0;


}