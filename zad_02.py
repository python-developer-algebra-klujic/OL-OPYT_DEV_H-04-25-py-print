'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost) 
te ispišite na ekran odgovarajuće vrijednosti, za:
    Stranice a i b, četverokuta te za površinu tog četverokuta.
    
    Izračun mjesečne potrošnje el. struje te cijene el. struje koju potroši 
    mikrovalna pećnica snage 1,3 kW ako se koristi 2 sata dnevno?
    
    Stranice trokuta, površinu trokuta (P = (𝑎 ∗ 𝑣_𝑎)/2, 𝑣_𝑎 je visina na stranicu a) te opseg trokuta.
'''

a = 5
b = 8

p = a * b


# Koristiti print funkciju koja ce ispisati ovu poruku:
# Povrsina cetverokuta stranica: a = [vrijednost varijable]; b = [vrijednost varijable] je: [vrijednost varijable].
print(f'Povrsina cetverokuta stranica: a = {a}; b = {b} je: {p}.') # trenutno zanemarite ovo je samo za provjeru rjesenja

# Kreirate privremene varijable koje sluze za pripremu prikaza poruke korisniku
first_part = 'Povrsina cetverokuta stranica: a = '
second_part = '; b = '
third_part = ' je: '
fourth_part = '.'

print(first_part, a, second_part, b, third_part, p, fourth_part, sep='')


# Unutar print() funkcije mozemo raditi i racunanje
print('Povrsina cetverokuta stranica: a = ', a, '; b = ', b, ' je: ', a * b, '.', sep='')



# Primjer kolege Denis Šragalj
print('Povrsina cetverokuta stranica: a = ', a, '; b = ', b, ' je: ', p, '.', sep='')

