x = 3

try:
    x / 0 # niemożliwa do wykonania próba dzielenia przez zero
    print(x)
except ZeroDivisionError: # fragment kodu informujący o błędzie
    print('Dzielenie przez zero') # print tego co wyświetlimy po napotkaniu na błąd
finally: # wymuszenie wykonania kodu pomimo wystąpienia wyjątku
    print('Dalsza część programu') # no i dalsza część programu
    print(x)

y = 5

try:
    y / 0
    print(y)
except ZeroDivisionError as blad: # różnica pomiędzy tym a poprzednim przykładem to przypisanie oryginalnej nazwy błędu do własnej nazwy
    print(blad) # no i print oryginalnej nazwy błędu zakodowanej pod przypisaną nazwą
finally:
    print('Dalsza część programu')
    print(y)