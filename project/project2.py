import string
from collections import Counter
import math

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

# process all books
def process_book(filename, start_line, end_line):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    text = ''.join(lines[start_line:end_line+1])
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    total_words = len(words)
    word_counts = Counter(words)
    return total_words, word_counts

books = {
    'Little Women': ('data/little women.txt', 656, 22498),
    'Pride and Prejudice': ('data/pride and prejudice.txt', 26, 14564),
    'The Brothers Karamazov': ('data/the brothers karamazov.txt', 26, 37287),
    'Dracula': ('data/Dracula.txt', 26, 15502),
}

data = {}
for title, (file, start, end) in books.items():
    total, counts = process_book(file, start, end)
    data[title] = {'total': total, 'counts': counts}

# Get all unique words
all_words = set()
for d in data.values():
    all_words.update(d['counts'].keys())

# Compute IDF
N = len(data)
idf = {}
for word in all_words:
    df = sum(1 for d in data.values() if word in d['counts'])
    idf[word] = math.log(N / df) if df > 0 else 0

# Compute TF-IDF for each book
tfidf_data = {}
for title, d in data.items():
    total = d['total']
    counts = d['counts']
    tfidf = {word: (counts[word] / total) * idf[word] for word in counts}
    tfidf_data[title] = tfidf

# Question 1: Which words are uniquely important to each book compared to the others?
print("\n=== Uniquely Important Words (Top 10 TF-IDF per book) ===")
for title, tfidf in tfidf_data.items():
    top_tfidf = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)[:10]
    print(f"\n{title}:")
    for word, score in top_tfidf:
        print(f"  {word}: {score:.4f}")

# Question 2: Identify words that appear frequently in one book but rarely in the others
print("\n=== Words Frequent in One Book but Rare in Others (High TF-IDF) ===")
# Already covered above, as high TF-IDF indicates that.

# Question 3: How does word usage differ across authors?
authors = {
    'Little Women': 'Louisa May Alcott',
    'Pride and Prejudice': 'Jane Austen',
    'The Brothers Karamazov': 'Fyodor Dostoyevsky',
    'Dracula': 'Bram Stoker',
}
print("\n=== Word Usage Differences Across Authors ===")
# Compare vocabulary sizes, unique words, etc.
for title, d in data.items():
    total = d['total']
    unique = len(d['counts'])
    diversity = unique / total if total > 0 else 0
    print(f"{title} ({authors[title]}): Total words: {total}, Unique words: {unique}, Diversity: {diversity:.4f}")

# Question 4: Compare how often specific keywords appear in each book
keywords = ['love', 'family', 'faith', 'money']
print("\n=== Keyword Frequencies ===")
for kw in keywords:
    print(f"\n{kw}:")
    for title, d in data.items():
        count = d['counts'].get(kw, 0)
        freq = count / d['total'] * 1000  # per 1000 words
        print(f"  {title}: {count} ({freq:.2f} per 1000 words)")

# Question 5: Which book has the most repetitive language?
print("\n=== Repetitiveness (Lower Diversity = More Repetitive) ===")
repetitiveness = {}
for title, d in data.items():
    total = d['total']
    unique = len(d['counts'])
    diversity = unique / total
    repetitiveness[title] = 1 - diversity  # Higher means more repetitive
    print(f"{title}: Diversity {diversity:.4f}, Repetitiveness {repetitiveness[title]:.4f}")

most_repetitive = max(repetitiveness, key=repetitiveness.get)
print(f"\nMost repetitive book: {most_repetitive}")

# Question 6: Analyze how concentrated the top words are within each text
print("\n=== Concentration of Top Words ===")
for title, d in data.items():
    total = d['total']
    counts = d['counts']
    top_100 = sum(count for word, count in counts.most_common(100))
    concentration = top_100 / total
    print(f"{title}: Top 100 words cover {concentration:.4f} of total words")

# Visualizations
import matplotlib.pyplot as plt

# Bar chart of top words for each book
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes = axes.flatten()
for i, (title, d) in enumerate(data.items()):
    counts = d['counts']
    top_10 = counts.most_common(10)
    words, freqs = zip(*top_10)
    axes[i].bar(words, freqs)
    axes[i].set_title(f'Top 10 Words in {title}')
    axes[i].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('top_words_barchart.png')
print("Saved top words bar chart to top_words_barchart.png")

# Comparison chart of vocabulary richness
titles = list(data.keys())
uniques = [len(d['counts']) for d in data.values()]
totals = [d['total'] for d in data.values()]
diversities = [u / t for u, t in zip(uniques, totals)]
plt.figure(figsize=(8, 6))
plt.bar(titles, diversities)
plt.title('Vocabulary Richness (Unique Words / Total Words)')
plt.ylabel('Diversity Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('vocabulary_richness.png')
print("Saved vocabulary richness chart to vocabulary_richness.png")


