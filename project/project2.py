import string
from collections import Counter

# Read the file
with open('data/little women.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract the main text: from line 657 to 22499 (0-based: 656 to 22498)
text = ''.join(lines[656:22499])

# Clean the text: lowercase, remove punctuation
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = text.split()

# Total word count
total_words = len(words)

# Count frequencies
word_counts = Counter(words)

# Top 20 most frequent words
top_20 = word_counts.most_common(20)

# Print results
print(f"Total word count: {total_words}")
print("Top 20 most frequent words:")
for word, count in top_20:
    print(f"{word}: {count}")


