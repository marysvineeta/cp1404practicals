FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        print(line)  # to See what a line looks like
        print(repr(line))  # to See what a line really looks like
        line = line.strip()  # to Remove the \n
        parts = line.split(',')  # to Separate the data into its parts
        print(parts)  # to See what the parts look like
        parts[2] = int(parts[2])  # to Make the number an integer
        data.append(parts)

    input_file.close()
    return data
