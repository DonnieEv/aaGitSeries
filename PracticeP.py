import string
from collections import Counter

text = "The quick brown fox jumps over the lazy dog. The dog barks!"

def word_stats(text):
    output = {}
  
    text1 = text.lower().strip().translate(str.maketrans('', '', string.punctuation)).split()
    count1 = Counter(text1).most_common(1)[0][0]
    avg_lent = round(sum(len(word) for word in text1) / len(text1), 2)
    output["# of words"] = len(text1)
    output["unique words"] =len(set(text1))
    output["The most common word is"] = count1
    output["Average length is "] = avg_lent
    return output

print(word_stats(text))
