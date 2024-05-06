#include <stdio.h>
int name(int v, int l)
{

    int answer = v + l;
    return answer;
}
int main()
{
    int a;
    a = name(50, 20);
    printf("%d", a);
    return 0;
}