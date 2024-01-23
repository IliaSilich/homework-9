def map_square(lst: list) -> list:
    return list(map(lambda x: x**2, lst))


original_list = [1, 2, 3, 4, 5]
squared_list = map_square(original_list)
print(squared_list)

