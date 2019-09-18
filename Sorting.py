def bubble_sort(A):
    length = len(A)
    for i in range(len(A)-1):
        for j in range(i+1, length):
            if A[i] > A[j]:
                A[i], A[j], = A[j], A[i]
    return A

print(bubble_sort([6,4,2,21,1]))