def quick_sort(S):
    if len(S) <= 1:
        return S
    left = []
    right = []
    pivot = S[0]  # left-most or right-most -> does not matter
    for element in S:
        if element >= pivot:
            right.append(element)
        else:
            left.append(element)
    left = quick_sort(left)
    right = quick_sort(right[1:])  # all elements but skipping index 0 (pivot - don't want to process further)
    return left + [pivot] + right


data = [85, 24, 63, 45, 17, 31, 96, 50]
data = quick_sort(data)
print(data)
