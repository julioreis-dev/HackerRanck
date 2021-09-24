def insert2(*args):
    args[2].insert(int(args[0]), int(args[1]))
    return args[2]

def remove2(*args):
    args[1].remove(int(args[0]))
    return args[1]

def append2(*args):
    args[1].append(int(args[0]))
    return args[1]

def sort2(*args):
    return args[0].sort()

def pop2(*args):
    return args[0].pop()

def reverse2(*args):
    return args[0].reverse()

def print2(*args):
    print(args[0])

def main(number_commands):
    list_command= []
    lista = []
    dispach = {'insert': insert2, 'remove': remove2, 'append': append2, 'sort': sort2, 'print': print2,
               'pop': pop2, 'reverse': reverse2}

    for n in range(number_commands):
        oper = list(input().split())
        list_command.append(oper)
    for t in list_command:
        if t[0] in ['remove', 'append']:
            dispach[t[0]](t[1], lista)
        elif t[0] in ['print', 'sort', 'pop', 'reverse']:
            dispach[t[0]](lista)
        else:
            dispach[t[0]](t[1], t[2], lista)

if __name__ == '__main__':
    N = int(input())
    main(N)
