def check_input(ch_str):
    if not ch_str.isnumeric():
        print('The number of pencils should be numeric')
        return False
    elif int(ch_str) == 0:
        print('The number of pencils should be positive')
        return False
    return True


def pencils_bot(n):
    if (n - 1) % 4 > 0:
        return (n - 1) % 4
    return 1


pencils = input('How many pencils would you like to use:')
while not check_input(pencils):
    pencils = input()
pencils = int(pencils)

persons = ('John', 'Jack')
first = input('Who will be the first (John, Jack):')
while first not in persons:
    first = input("Choose between 'John' and 'Jack'")
turn = persons.index(first)

print(''.join('|' * pencils))
while pencils > 0:
    if turn % 2 == 0:
        minus_pencil = input(f"{persons[turn % 2]}'s turn!")
        while minus_pencil not in ('1', '2', '3'):
            minus_pencil = input("Possible values: '1', '2' or '3'")
        while int(minus_pencil) > pencils:
            minus_pencil = input("Too many pencils were taken")
    else:
        print("Jack's turn:")
        minus_pencil = pencils_bot(pencils)
        print(minus_pencil)
    turn += 1
    pencils -= int(minus_pencil)
    print(''.join('|' * pencils))

print(f'{persons[turn % 2]} won!')
