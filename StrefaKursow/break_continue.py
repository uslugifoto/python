# zwracanie na ekran zakresu liczb 1 - 100

a = 0
while a < 100: # pętla "while" działa dopóki "a" jest mniejsze niż 100
    a += 1 # operacja dekrementacji
    print(a)

# zwracanie zakresu liczb 1 - 100, ale przerwane przez break na 50
b = 0
while b < 100:
    b += 1
    print(b)
    if b == 50: # zagnieżdżona instrukcja warunkowa "if", w jakim momencie pętla ma być przerwana
        break

# zwracanie zakresu liczb 1 - 100, ale tylko parzystych
c = 0
while c < 100:
    c += 1
    if c % 2 != 0: # operator "%" zwraca resztę z dzielenia, jesli nie ma reszty przy dzieleniu przez 2...
        continue #... kontynuuj
    print(c)