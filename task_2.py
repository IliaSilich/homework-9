def sort_by_length(lst: list) -> list:
    return sorted(lst, key=len)


original_list = ["apple", "banana", "cherry", "date"]
sorted_list = sort_by_length(original_list)
print(sorted_list)
