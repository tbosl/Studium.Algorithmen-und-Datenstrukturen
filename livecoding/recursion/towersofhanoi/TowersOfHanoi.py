def towers_of_hanoi(n, src='A', tar='C', aux='B'):
    if n == 1:
        print('Move disk 1 from {0} to {1}'.format(src, tar))
        return
    towers_of_hanoi(n - 1, src, aux, tar)
    print('Move disk {0} from {1} to {2}'.format(n, src, tar))
    towers_of_hanoi(n - 1, aux, tar, src)


print(towers_of_hanoi(2))
print(towers_of_hanoi(5))
