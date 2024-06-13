def main():
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)

def get_password(min_length):
    while True:
        password = input("Enter a password: ")

        if len(password) >= min_length:
            return password
        else:
            print(f"Password must be at least {min_length} characters long. Please try again.")

def print_asterisks(password):
    print('*' * len(password))

if __name__ == "__main__":
    main()



