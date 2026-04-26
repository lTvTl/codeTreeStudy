a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def dohagi(a, c):
    return print(a,'+', c,'=', a + c)

def pegi(a, c):
    return print(a,'-', c,'=', a - c)

def nanugi(a, c):
    return print(a,'/', c,'=', a // c)

def goup(a, c):
    return print(a,'*', c,'=', a * c)


if o == '+':
    dohagi(a, c)
elif o == '-':
    pegi(a, c)
elif o == '/':
    nanugi(a, c)
elif o == '*':
    goup(a, c)
else:
    print('False')

