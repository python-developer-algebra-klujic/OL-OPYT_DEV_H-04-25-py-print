'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost) 
te ispišite na ekran odgovarajuće vrijednosti, za:
    Ime, prezime, godinu rođenja, državu rođenja, status radnog odnosa, težinu te spol
'''

first_name = 'Pero'
last_name = 'Peric'
dob = 1999
country = 'Hrvatska'
is_employed = True
weight = 90.59
gender = 'male'

print()                                         # \n
print('Ime:', first_name, end='; ')             # \n -> ; 
print('Prezime:', last_name)                    # \n
print('Godina rodenja:', dob)                   # \n
print('Drzava rodenja:', country)               # \n
print('Radni status:', is_employed)             # \n
print('Tezina:', weight)                        # \n
print('Spol:', gender)                          # \n
print()                                         # \n

# print("Hello", end=" ")

# Bojan Kuljić: print('Ime:', first_name, end='; ' + last_name) -> ne radi jer nakon end= ne dodajemo nove vrijednosti
# Verzija koja radi:
print('Ime:' + first_name + ' ' + last_name, 'druga vrijednost', end='; ')

# 'Ime:' + first_name + ' ' + last_name
# 'Ime:' + 'Pero' + ' ' + 'Peric' - > 'Ime:Pero Peric'
