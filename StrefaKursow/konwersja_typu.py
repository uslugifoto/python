print('---')
x = 1
print('x = 1')
print(x)
print(type(x))
print('---')

x = float(x)
print('x jako 1 zamienione na float, czyli 1.0')
print(x)
print(type(x))
print('---')

x = str(x)
print('x jako 1.0 float zamienione na string, czyli ciąg znaków "1.0" i dodanie do siebie')
print(x + x)
print(type(x))
print('---')

y = 1
print('y = 1')
print(y)
print(type(y))
print('---')

y = hex(y)
print('y jako 1 zamienione na hex, czyli 0x1, uwaga hex to string')
print(y)
print('a jak wiemy dodawanie stringów to konkatenacja')
print(type(y))
print(y + y)
print('---')

v = 1
print('v = 1')
print(v)
print(type(v))
print('---')

v = bin(v)
print('v jako 1 zamienione na bin, czyli 0b1, uwaga bin to string')
print(v)
print(type(v))
print('---')

print(x + x)