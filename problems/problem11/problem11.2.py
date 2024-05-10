def merge_sort(S):
    n = len(S)
    if n < 2:
        return  # already sorted with 0 or 1 element
    mid = n // 2
    S1 = S[:mid]  # from 0 to mid excluded
    S2 = S[mid:]  # mid included to last
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)
    return S


def merge(S1, S2, S):
    # pass  # TODO
    # i = 0
    # j = 0
    # for k in range(i+j):
    #     if <= für stable?
    i = 0
    j = 0
    for k in range(len(S1) + len(S2)):
        if i == len(S1):
            S[k] = S2[j]
            j += 1
            continue
        elif j == len(S2):
            S[k] = S1[i]
            i += 1
            continue
        if S1[i] <= S2[j]:
            S[k] = S1[i]
            i += 1
        else:
            S[k] = S2[j]
            j += 1


data = [85, 24, 63, 45, 17, 31, 96, 50]
print(merge_sort(data))
