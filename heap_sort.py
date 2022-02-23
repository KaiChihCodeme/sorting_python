# Heapify means 排列成Heap的規則之結構
# To heapify subtree rooted at index i
# n is size of heap
def maxHeapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # heap子節點為2，因此i的左子節點 2i+1
    r = 2 * i + 2  # 同上，右子節點為2i+2
  
    # see if left child of root exists and is greater than root (確認最大值是否在子節點，是的話會在下面更動)
    if l < n and arr[i] < arr[l]:  # l<n是為了確定他沒有超出array範圍，arr[i]<arr[l]則是確認root and left child
        largest = l
  
    # see if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # change root if needed (largest not root)，交換位置，因為只有更動index。更動完再遞迴往下檢查
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]

        # Heapify root  (最大值更動，再檢查一次最大值這邊有沒有是在父節點了)
        maxHeapify(arr, n, largest)
  
def heapSort(arr):
    n = len(arr)

    # Build a msxheap.
    # Since last parent will be at (n//2-1) we can start at that location
    for i in range(n // 2 - 1, -1, -1):  # 他是三個node一起看，因此只要是在非leaf node的位置都traverse一次
        maxHeapify(arr, n, i)
  
    # Change Maximum to the last, then reorder again within loop, we will get the ordered one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)

data = [30,20,15,1,10,5]
heapSort(data)
print(data)