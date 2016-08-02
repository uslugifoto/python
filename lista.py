# tworzenie listy

Lista = ["PKP", "PLK", "PLL", "PIS"]

# drukowanie elementu listy (tu akurat pierwszej pozycji)

print(Lista[0])

# drukowanie liczby pozycji na liście

print(len(Lista))

# drukowanie ostatniej pozycji listy

print(Lista[len(Lista) - 1])

# dodawanie pozycji do listy

Lista.append("PHP")

# ponowne drukowanie ostatniej pozycji listy po dodaniu pozycji

print(Lista[len(Lista) - 1])


# drukowanie zawartości listy od 2 do 4
print(Lista[1:4])

# usuwa drugą pozycje z listy

Lista.__delitem__(1)

# ponownie, juz po odjeciu pozycji, drukuje druga pozycje z listy

print(Lista[1])

Lista.append("PIP")

print(Lista)

Lista.remove("PIP")

print(Lista)

x = "Ala ma kota, a kot ma Alę :3"

a = x[1:]
b = x[2:]
c = x[3:]
d = x[4:]
e = x[5:]
f = x[6:]
g = x[7:]
h = x[8:]
i = x[9:]
j = x[10:]
k = x[11:]
l = x[12:]

print(x)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(x)