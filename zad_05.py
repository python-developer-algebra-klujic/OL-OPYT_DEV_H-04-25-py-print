'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:
    Ako automobil troši 5.3 litara na 100 km i ako je cijena goriva 9.56 kn po litri (nije važno kojeg goriva), 
    izračunajte koliko košta 1 km vožnje automobilom. 
    Prikažite mjesečni trošak (30 dana) odlaska na posao automobilom koji je udaljen 20 km u jednom smjeru.
'''

# Ulazni podaci
fuel_consumption = 5.3      # litara na 100 km
fuel_price = 1.56           # EUR / litra
distance_one_way = 20       # km
days_in_month = 30


# Izracuni -> glavni dio programa
fuel_per_km = fuel_consumption / 100             # litara po km
cost_per_km = fuel_per_km * fuel_price           # EUR po km

daily_distance = distance_one_way * 2            # povratno
daily_cost = daily_distance * cost_per_km        # EUR po danu
monthly_cost = daily_cost * days_in_month        # EUR mjesecno


# Ispis
print('Cijena po km (EUR):', round(cost_per_km, 2))
print('Dnevni trošak odlaska na posao (EUR):', round(daily_cost, 2))
print('Mjesečni trošak (EUR):', round(monthly_cost, 2))
