# Program rozgałęziony
print ("Ten program porównuje dwie liczby")
x = input("Podaj pierwszą z dwóch liczb:")
y = input("Podaj drugą z dwóch liczb:")
x = eval(x)
y = eval(y)
print ("Liczba",x,"w stosunku do",y,"jest:", end = " ")   # Przecinek!
if x==y:
    print ("taka sama")
elif x>y:
    print ("większa")
else:
    print ("mniejsza")