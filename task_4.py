def count_vowels(s: str, case_sensitive: bool) -> int:
    vowels = set("aeiou" if not case_sensitive else "aeiouAEIOU")
    s = set(s.lower()) if not case_sensitive else set(s)

    unique_vowels = vowels.intersection(s)
    return len(unique_vowels)


result = count_vowels("Hello, world!", case_sensitive=True)
print(result)
