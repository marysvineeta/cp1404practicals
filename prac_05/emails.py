"""
Email and Name Directory
Estimate: 30 minutes
Actual:   35 minutes
"""

def main():
    user_directory = {}

    email = input("Email: ")
    while email:
        suggested_name = generate_name_from_email(email)
        confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()
        if confirmation not in ["y", ""]:
            suggested_name = input("Name: ").strip()
        user_directory[email] = suggested_name
        email = input("Email: ")

    print("\n")
    for email, name in user_directory.items():
        print(f"{name} ({email})")

def generate_name_from_email(email):
    username = email.split('@')[0]
    name_parts = username.split('.')
    generated_name = " ".join(name_parts).title()
    return generated_name

if __name__ == "__main__":
    main()
