/* Sum and Difference of Two Numbers in C */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int i,j;
    float n,m;
    scanf("%d %d %f %f\n", &i, &j, &n, &m);
    printf("%d %d\n%.1f %.1f\n", i+j, i-j, n+m, n-m);

    return 0;
}
