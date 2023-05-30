#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
void main()
{
    char str[]  = "HelloWorld";
    char str1[11],str2[11];
    int len ;
    len  = strlen(str);
    for (int i = 0; i < len; i++)
    {
        str1[i]  = str[i] & 127;
        printf("%d",str1[i]);
        /* code */
    }
    
    printf("\n");
        for (int i = 0; i < len; i++)
    {
        str2[i]  = str[i] ^ 127;
        printf("%d",str2[i]);
        /* code */
    }
    
    printf("\n");
    

}
