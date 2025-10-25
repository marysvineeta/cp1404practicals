"""
Word Occurrences
Estimate: 25 minutes
Actual:   28 minutes
"""

def main():
    """Count the occurrences of words"""
    text = input("Text: ")
    words = text.split()
    word_to_count = {}

    # Count each word
    for word in words:
        word = word.lower()
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    sorted_words = sorted(word_to_count.keys())

    # Find the longest word
    max_length = max(len(word) for word in sorted_words)

    # Display words and their counts
    for word in sorted_words:
        print(f"{word:{max_length}} : {word_to_count[word]}")


main()
