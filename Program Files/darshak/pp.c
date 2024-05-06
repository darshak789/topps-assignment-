#include <stdio.h>
int main()
{
    int k = 1;
    for (int i = 1; i <= 5; i++)
    {
        for (int i = 1; i <= k; i++)
        {
            printf(" * ");
        }
        k++;
        printf("\n");
        
    }

    return 0;
}
