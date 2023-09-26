
# def factorial(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n-1)


# if __name__ == "__main__":
#     print(factorial(999))

# -----------------------------------------------------------------------#


def example_recur(b):
    if b > 50:
        return 15
    else:
        return 2 + example_recur(b + 23)


if __name__ == "__main__":

    b = int(input("Type your number: "))
    print(example_recur(b))
