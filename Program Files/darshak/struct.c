#include <stdio.h>
struct student
{
    int rollno;
    char name[50];
    int age;
    char address[50];
    float percetage;
    char subject[50];
};

int main()
{
    struct student s[3];
    for (int i = 0; i < 3; i++)
    {

        printf("enter the roll no:");
        scanf("%d", &s[i].rollno);

        printf("enter the name:");
        scanf(" ");
        gets(s[i].name);

        printf("enter the age:");
        scanf("%d", &s[i].age);

        printf("enter the address:");
        scanf(" ");
        gets(s[i].address);

        printf("enter the percetage:");
        scanf("%f", &s[i].percetage);

        printf("enter the subject:");
        scanf("%s", &s[i].subject);
    }

    printf("\n--------- all data---------\n");
    for (int i = 0; i < 3; i++)
    {
        printf("name=%s\nrollno=%d\nage=%d\naddress=%s\npercetage=%f\nsubject=%s\n", s[i].name, s[i].rollno, s[i].age, s[i].address, s[i].percetage, s[i].subject);
    }
    return 0;
}