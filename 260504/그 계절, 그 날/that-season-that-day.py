Y, M, D = map(int, input().split())

# Please write your code here.
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def nuen(y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            return False
        return True

def season(M):
    if M >= 3 and M <= 5:
        return 1
    elif M >= 6 and M <= 8:
        return 2
    elif M >= 9 and M <= 11:
        return 3
    elif M == 1 or M == 2 or M == 12:
        return 4
    

def thisDay(Y, M, D):
    if nuen(Y) == True:
        month[1] = 29
    if M >= 1 and M <= 12:
        if D >= 1 and D <= month[M-1]:
            if season(M) == 1:
                return print("Spring")
            elif season(M) == 2:
                return print("Summer")
            elif season(M) == 3:
                return print("Fall")
            elif season(M) == 4:
                return print("Winter")
    return print("-1")

thisDay(Y, M, D)