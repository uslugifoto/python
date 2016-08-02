# Wpisujemy z palca jakąś liczbę x i y, za każdym razem one nam się drukują, po czm otrzymujemy rezultat w postaci połączenia dwóch "str" (nie wynik)


x = input("Wpisz pierwszą: ")

print(x)

y = input("Wpisz drugą liczbę: ")

print(y)

z = x + y

# Drukujemy typ i widzimy że wynik to "str"

print(type(z))

print(z)

# Zamieiamy x i y z "str" na "float"

x = float(x)

y = float(y)

# Drukujemy typ

print(type(z))

# Sumujemy i otrzymujemy wynik oraz typ "float"

z = x + y

print(z)

print(type(z))
