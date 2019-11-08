// 1D Arrays in C:

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,sum = 0;
    scanf("%d", &n);
    int *val = (int*)malloc (n * sizeof(int));
    for(int i=0;i<n;i++)
    {
        scanf("%d", &val[i]);
        sum += val[i];
    }
    printf("%i", sum);
    free(val);    
    
    return 0;
}
