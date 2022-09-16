#include <stdio.h>
#include <string.h>

int dump(char* str)
{
    strcpy(str, "Hello, world!");
    return (int)strlen(str);
}

int add(int a, int b)
{
    return a+b;
}