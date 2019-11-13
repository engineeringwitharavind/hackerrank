/* Caluclate the nth term - Recursion */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int find_nth_term(int n, int a, int b, int c)
{
  int add = 0;
  add = a + b + c;
  return add + c + b;
}

int main()
{
  int n, a, b, c;
  
  scanf("%d %d %d %d", &n, &a, &b, &c);
  int ans = find_nth_term(n, a, b, c);
  printf("%d", ans);
  return 0;
}
