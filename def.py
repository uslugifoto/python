def powiedz_czesc():
    print("Cześć!")
powiedz_czesc()

def add(a, b, c):
    return a + b + c
x = add(1, 3, 5)
print(x)

def cyfry(*args):
    print(args)
    return sum(args) / len(args)
x = cyfry(2, 2, 2, 2, 2, 2, 2)
print(x)
