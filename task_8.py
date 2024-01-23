def recursive_sum(lst):
    total = 0

    for element in lst:
        if isinstance(element, list):
            total += recursive_sum(element)
        elif isinstance(element, (int, float)):
            total += element
        else:
            raise ValueError("Список содержит не числовые значения")

    return total


nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, "10"]]]

try:
    result = recursive_sum(nested_list)
    print(result)
except ValueError as e:
    print(e)
