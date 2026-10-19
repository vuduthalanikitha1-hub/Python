def remove_duplicates(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if word not in result:
            result.append(word)

    return " ".join(result)

text = "python is easy python is powerful"
print(remove_duplicates(text))
