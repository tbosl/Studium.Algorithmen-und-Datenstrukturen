def fib_bottom(n):
    if n == 0:
        return 0
    prev_fib = 0
    current_fib = 1
    for i in range(n - 1):
        new_fib = prev_fib + current_fib
        prev_fib = current_fib
        current_fib = new_fib
    return current_fib


print(fib_bottom(20577))
