#include <stdio.h>
#include <string.h>
int main()
{
    int ansewr;
    char string1[20] = "zebra";
    char string2[20] = "zebra";
    ansewr = strcmp(string1, string2);
    printf("your answer is %d", ansewr);
    return 0;
}