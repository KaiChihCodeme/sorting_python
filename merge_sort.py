def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2

        L = arr[:mid]  # dividing array elements 切分為左右兩陣列
        R = arr[mid:]  # the last part

        # Sorting the first half  繼續切，從左邊開始
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0  # i代表左半邊的index, j代表右半邊, k則代表temp array index

        # Copy Data to temp array L[] and R[] (用指標去比較，若左邊小於右邊是正常的，左邊加入tmp array後左邊指標向下。若大於右邊，則應該將右邊先加入tmp array)在移動
        # 右邊index。k則用來紀錄新的merge sorted array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left  
        # 若左邊或右邊還有elements沒用到，就直接由左到右把他依序排上tmp array（為啥可以依序？因為他們在上一個回圈左右兩邊都被排好了）
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print('Given array is', end='\n')
    printList(arr)
    mergeSort(arr)
    print('Sorted array is', end='\n')
    printList(arr)
