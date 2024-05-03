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


def merge(S1, S2, S):
    pass  # TODO
    # i = 0
    # j = 0
    # for k in range(i+j):
    #     if <= für stable?


data = [85, 24, 63, 45, 17, 31, 96, 50]
