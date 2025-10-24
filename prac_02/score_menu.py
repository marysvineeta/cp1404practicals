import random


def main():
    """Main function to run the score menu program."""
    score = get_valid_score()
    choice = display_menu()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")

        choice = display_menu()

    print("Farewell!")


def display_menu():
    """Display menu and get user's choice."""
    print("\n(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input(">>> ").upper()
    return choice


def get_valid_score():
    """Get a valid score (0–100 inclusive)."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score


def get_score_result(score):
    """Return the status of a score as text."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print as many stars as the score."""
    print('*' * int(score))


main()
