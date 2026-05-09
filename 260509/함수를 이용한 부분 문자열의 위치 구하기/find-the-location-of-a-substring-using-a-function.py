text = input()
pattern = input()

# Please write your code here.
a = len(text)
b = len(pattern)
def sum_all():
    if pattern in text:
        for i in range(a):
            if text[i:i+b] == pattern:
                return print(i)
    else:
        return print(-1)

sum_all()