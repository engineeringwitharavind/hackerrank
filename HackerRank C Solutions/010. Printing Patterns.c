/* Printing Patterns using loops in C */

#include <stdio.h>
int main() 
{
    int n;
    scanf("%d", &n);
    int len = 2 * n - 1;
    int min1, min2, min;
    for (int i = 1; i <= len; i++)  // For Rows 
    {
      for (int j = 1; j <= len; j++) // For Columns
      {
        // Minimum difference between Vertical sides  
        min1 = i <= len - i ? i -1 : len - i; 
        // Minimum difference between Horizontal sides
        min2 = j <= len - j ? j - 1: len - j;
        // Minimum difference between Horizontal and Vertical sides
        min = min1 <= min2 ? min1 : min2; 
        printf("%d ",n - min);
      }
      printf("\n");
  }
return 0;
}
