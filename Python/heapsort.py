# Heap Sort in python
def heap(arr, n, i):
      # Find largest among root and children
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heap(arr, n, largest)
  
def heapSort(arr):
      n = len(arr)
  
      
      for i in range(n//2, -1, -1):
          heap(arr, n, i)
  
      for i in range(n-1, 0, -1):
         
          arr[i], arr[0] = arr[0], arr[i]
  
         
          heapify(arr, i, 0)
  
  
arr = [61, 25, 9, 7, 39, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
     print("%d " % arr[i], end='')
