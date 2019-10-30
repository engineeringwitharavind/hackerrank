/* HackerRank C - Playing with Characters. */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    char ch;
    char s[15];
    char sen[100];
    scanf("%c\n", &ch);
    printf("%c\n", ch);
    scanf("%[^\n]%*c", &s);
    printf("%s\n", s);
    scanf("%[^\n]%*c\n", &sen);
    printf("%s\n", sen);
    
    return 0;
}