def reverse_number(n: int, reversed_n: int = 0) -> int:
    if n == 0:
        return reversed_n
    else:
        last_digit = n % 10
        reversed_n = reversed_n * 10 + last_digit
        return reverse_number(n // 10, reversed_n)


number = 12345
reversed_number = reverse_number(number)
print(reversed_number)
