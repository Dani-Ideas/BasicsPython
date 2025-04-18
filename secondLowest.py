import csv

def print_second_lowest_students_from_csv(file_path):
    students = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            score = float(row[1])
            students.append([name, score])

    scores = sorted({s[1] for s in students})
    second_lowest = scores[1]

    result = sorted([s[0] for s in students if s[1] == second_lowest])

    for name in result:
        print(name)
