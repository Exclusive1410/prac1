file = open('text.txt')

lines = 0
words = 0
letters = 0

for line in file:
    lines += 1

    for symbol in line:
        if symbol not in (' ', '\n', '\t'):
            letters += 1

    pos = 'out'
    for symbol in line:
        if symbol != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif symbol == ' ':
            pos = 'out'

print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)