#include <stdio.h>
void table(int z)
{
    int num, i;
    printf("enter the num:");
    
    scanf("%d", &num);

    for (int i = 1; i < 11; i++)

    {
        printf("%d X %d =%d\n", num, i, num * i);
    }
}
int main()
{
    int i = 40;
    table(i);

    return 0;
}