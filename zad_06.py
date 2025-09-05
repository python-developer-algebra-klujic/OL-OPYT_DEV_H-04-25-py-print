'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:

    Imate 10000 kn i možete zaboraviti na njih na 15 godina. 
    Ako Vam banka nudi 2.5% godišnju kamatu za taj iznos, koliko ćete zaraditi nakon 15 godina. 
    Jednostavni kamatni račun k = C * p * t
        k = iznos kamata odnosno prinos
        C = iznos glavnice
        p = godišnja kamatna stopa – NAPOMENA: 5% = 5 / 100 = 0.05
        t = vrijeme u godinama
'''

# Ulazni podaci
principal = 10000           # kn (glavnica)
interest_rate = 2.5 / 100   # godisnja stopa
time_years = 15             # godina

# Izracuni
interest = principal * interest_rate * time_years
final_amount = principal + interest

# Ispis
print('Zarada od kamata (kn):', round(interest, 2))
print('Ukupni iznos nakon 15 godina (kn):', round(final_amount, 2))
