#include <stdio.h>
void addition()
{
    int a, b, answer;
    printf("enter two value:");
    scanf("%d %d", &a, &b);
    answer = a + b;
    printf("addition=%d ", answer);
}
void subtraction()
{
    int a, b, answer;
    printf("enter two value:");
    scanf("%d %d", &a, &b);
    answer = a - b;
    printf("subtraction=%d ", answer);
}
void multiplion()
{
    int a, b, answer;
    printf("enter two value:");
    scanf("%d %d", &a, &b);
    answer = a * b;
    printf("multiplion=%d ", answer);
}
void divison()
{
    int a, b, answer;
    printf("enter two value:");
    scanf("%d %d", &a, &b);
    answer = a / b;
    printf("divison=%d ", answer);
}
int main()
{
    int choice, num;
    printf("1-addition\n2-subtraction\n3-multiplion\n4-divison\n ");
    printf("\n enter your choice ");
    scanf("%d", &choice);
    switch (choice)
    {
    case 1:
    {
        addition();
        break;
    }
    case 2:
    {
        subtraction();
        break;
    }
    case 3:
    {
        multiplion();
        break;
    }
    case 4:
    {
        divison();
        break;
    }
    }
}