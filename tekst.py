# apostrof ' poprzedzony backslashem powoduje że jest on traktowany jak normalny tekst

tekst = "ala\'s ma kota"

print(tekst)

# "r" przed powoduje że ten sam backslash staje się zwykłym elementem tekstu

tekst = r"ala\'s ma kota"

print(tekst)

# wyrzuca czwarty znak z tekstu, trzeba pamiętać że pierwszy znak to "0"
tekst = "ala ma kota a kot ma Ale"

print(tekst[4])

#wyrzuca znaki od czwartego do szóstego włącznie, trzeba pamiętać że pierwszy znak to "0"

print(tekst[4:7])

#wyrzuca znaki od czwartego do końca, trzeba pamiętać że pierwszy znak to "0"

print(tekst[4:])

#wyrzuca od pierwszego do trzeciego znaku, trzeba pamiętać że pierwszy znak to "0"

print(tekst[:3])

#wyrzuca drugi znak od końca

print(tekst[-2])

#wyrzuca długość tekstu

print(len(tekst))

#wyrzuca teks zaczynając go od dużej litery

print(tekst.capitalize())