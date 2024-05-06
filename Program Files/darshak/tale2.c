#include <stdio.h>
void table(int num)
{

    for (int i = 1; i < 11; i++)

    {
        printf("%d X %d =%d\n", num, i, num * i);
    }
}
int main()
{

    table(1);
    table(2);
    table(3);
    table(4);
    table(5);
    table(6);
    table(7);
    table(8);
    table(9);
    table(10);

    return 0;
}