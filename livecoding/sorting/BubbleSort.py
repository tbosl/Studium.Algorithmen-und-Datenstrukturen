def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - i - 1):  # optimized by -i as rightmost element greatest after 1st and so on..
            if A[j] > A[j + 1]:
                tmp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = tmp


data = [5, 3, 8, 4, 6]
bubble_sort(data)
print(data)
