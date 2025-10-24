FILENAME = "subject_data.txt"


def main():
    """Read subject data and display details """
    subject_details = load_subject_details(FILENAME)
    display_subject_details(subject_details)


def load_subject_details(filename):
    """Read data from file and return list """
    subject_details = []
    input_file = open(filename, "r")
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])  # convert number of students to int
        subject_details.append(parts)
    input_file.close()
    return subject_details


def display_subject_details(subject_details):
    """Display all subject details """
    for subject, lecturer, students in subject_details:
        print(f"{subject} is taught by {lecturer} and has {students} students")


main()
