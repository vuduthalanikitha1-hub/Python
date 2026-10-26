def character_frequency(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    return freq

print(character_frequency("banana"))