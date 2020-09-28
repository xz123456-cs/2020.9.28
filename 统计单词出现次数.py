lyric = 'The night begin to shine, the night begin to shine'
words = lyric.split()

from collections import Counter
res = Counter(words)
print(res)