if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    listgrade = student_marks[query_name]
    sum1 = 0
    for grade in listgrade:
        sum1 = sum1 + grade
    media = sum1/len(listgrade)
    print(f'{media:.2f}')
