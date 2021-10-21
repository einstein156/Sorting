def insertion(arr):
   for i in range(1, len(arr)):
      key = arr[i]


      j = i-1
      
      
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         j -= 1
        
      arr[j+1] = key

      
arr = [4,34,5,6,67,987,123,23,32]

insertionSort(arr)

print ("sorted array:")
for i in range(len(arr)):
   print (arr[i])
