def power(x: float, y: int) -> float:
    if y == 0:
        return 1
    elif y > 0:
        return x * power(x, y - 1)
    else:
        if x == 0:
            raise ValueError("Ноль в отрицательной степени не определен")
        return 1 / power(x, -y)


print(power(2, 3))
print(power(2, 0))
print(power(2, -2))
print(power(0, 2))

try:
    print(power(0, -2))
except ValueError as e:
    print(e)
