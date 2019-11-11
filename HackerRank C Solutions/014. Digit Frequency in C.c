// Digit Frequency in C:

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    
    char s;
    int i,a[] ={0,0,0,0,0,0,0,0,0,0};
    while(scanf("%c", &s) == 1)
        if(s >= '0' && s <= '9')
            a[s-'0'] += 1;
    for(i=0; i<10; i++)
        printf("%d ", a[i]);
    
    return 0;
}
