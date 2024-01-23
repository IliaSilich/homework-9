def modify_list(lst: list, *funcs: callable) -> None:
    for i in range(len(lst)):
        for func in funcs:
            lst[i] = func(lst[i])


def square_even(x: list) -> list:
    return x**2 if x % 2 == 0 else x


def increment_odd(x: list) -> list:
    return x + 1 if x % 2 != 0 else x


def multiply_by_3_if_prime(x: list) -> list:
    if x < 2:
        return x
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return x
    return x * 3


my_list = [1, 2, 3, 4, 5]
modify_list(my_list, square_even, increment_odd, multiply_by_3_if_prime)
print(my_list)
