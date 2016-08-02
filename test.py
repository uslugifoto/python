print("Ile należy dodać do 7 żeby uzyskać liczbę 10?")

y = input("Wpisz liczbę: ")

y = float(y)

x = 7+y



if x == 10:
    print("Brawo :)")

else:
    print("Spróbuj jeszcze raz :(")

print("Twój wynik to: ")
x = str(x)
print(x[:-2])

print("")
print("Gotowe")