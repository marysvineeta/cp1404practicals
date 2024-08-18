"""
Word Occurrences
Estimate: 25 minutes
Actual:   34 minutes
"""

def main():
    text = input("Text: ")
    word_counts = {}

    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    longest_word_length = max(len(word) for word in word_counts.keys())
    sorted_word_counts = dict(sorted(word_counts.items()))

    for word, count in sorted_word_counts.items():
        print(f"{word:{longest_word_length}} : {count}")

if __name__ == "__main__":
    main()
