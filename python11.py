def count_letters(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    return upper, lower

u, l = count_letters("Hello PYTHON World")
print("Uppercase:", u)
print("Lowercase:", l)