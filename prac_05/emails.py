"""
Emails
Estimate: 25 minutes
Actual:   30 minutes
"""


def main():
    """Store emails in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y"):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    # Display stored names and emails
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from the given email address."""
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').split()
    name = " ".join(parts).title()
    return name


main()
