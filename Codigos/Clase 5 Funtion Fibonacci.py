
# f0 = 0
# f1 = 1
# f2 = f1 + f0 = 1 + 0 = 1
# f3 = f2 + f1 = 1 + 1 = 2
# f4 = f3 + f2 = 2 + 1 = 3

def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return None
    if n < 3:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    print(fibonacci(4))
