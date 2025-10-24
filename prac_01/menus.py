
name = input("Enter name: ")

# Display menu options
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = input(">>> ").upper()

# Loop
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Re-display menu
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()

print("Finished.")
