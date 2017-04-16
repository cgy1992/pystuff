with open('a.txt', 'w') as a, open('b.txt', 'w') as b:
    for i in (a, b):
        i.write('text')