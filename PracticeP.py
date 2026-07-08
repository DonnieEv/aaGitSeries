import string

def top_n_words(text, n):
    dict1 = {}
    words = text.lower().split()
    for word in words:
        word = word.translate(str.maketrans('', '', string.punctuation))
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1

    sorted_words = sorted(dict1.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:n]

text = "The quick brown fox jumps over the lazy dog. The dog barks!"

print(top_n_words(text, 2))
