#include <stdio.h>
int main()
{

    int Arr1[2][2], Arr2[2][2], Multi[2][2], r, c;
    printf("Enter the Row:\n");
    scanf("%d", &r);

    printf("Enter the Collum:\n");
    scanf("%d", &c);

    printf("\nEnter the first matrix elements:");

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            scanf("%d", &Arr1[i][j]);
        }
    }

    printf("\nEnter the second matrix elements:");

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            scanf("%d", &Arr2[i][j]);
        }
    }

    printf("\nMultiply of the matrix:\n");

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            Multi[i][j] = 0;
            for (int k = 0; k < c; k++)
            {
                Multi[i][j] += Arr1[i][k] * Arr2[k][j];
            }
        }
    }

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("%d\t", Multi[i][j]);
        }
    }

    return 0;
}