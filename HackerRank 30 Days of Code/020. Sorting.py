#!/bin/python3
import sys

def bubble_sort(n, arr):
  num_of_swaps = 0
  for i in range(n):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        num_of_swaps += 1
  return num_of_swaps

if __name__ == "__main__":
  n = int(input().strip())
  arr = list(map(int, input().strip().split(' ')))
  swaps = bubble_sort(n, arr)
  print("Array is sorted in", swaps, "swaps.")
  print("First Element:", arr[0])
  print("Last Element:", arr[-1])
