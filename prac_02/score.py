import random


def main():
    """Get user's score, print result, and show random score result."""
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)

    # Generate a random score and display the result using the same function
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(get_score_result(random_score))


def get_score_result(score):
    """Determine the status of a given score and return it as text."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
