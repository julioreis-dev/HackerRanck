# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stud = [name, score]
        students.append(stud)
    grades = sorted(set([x[1] for x in students]))
    candidates = sorted([x[0] for x in students if x[1] == grades[1]])
    for i in candidates:
        print(i)
