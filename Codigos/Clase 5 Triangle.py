def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


def is_rectangle(a, b, c):
    if is_triangle(a, b, c):
        if a*a == b*b+c*c:
            print("is a triangle rectangle")
        elif b*b == a*a+c*c:
            print("is a triangle rectangle")
        else:
            print("Not is a triangle rectangle")

    else:
        print("Not is a triangle rectangle 2")


def is_rectangle2(a, b, c):
    if not is_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


if __name__ == '__main__':
    print(is_triangle(39.12,33, 21))
    is_rectangle(39.12,33, 21)
    print(is_rectangle2(39.12,33, 21))
