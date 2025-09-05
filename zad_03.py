'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost) 
te ispišite na ekran odgovarajuće vrijednosti, za:
    Izračun mjesečne potrošnje el. struje te cijene el. struje koju potroši 
    mikrovalna pećnica snage 1,3 kW ako se koristi 2 sata dnevno?
'''

monthly_avg_days = 30   # dana
el_price = 1.99         # EUR / kWh
mw_power = 1.3          # kW
daily_usage = 2         # h

daily_consumption = mw_power * daily_usage                      # kWh
monthly_consumption = daily_consumption * monthly_avg_days      # kWh

daily_price = daily_consumption * el_price
monthly_price = monthly_consumption * el_price

print('Dnevna potrosnja (kWh):', daily_consumption)
print('Mjesečna potrosnja (kWh):', monthly_consumption)
print('Dnevna cijena (EUR):', daily_price)
print('Mjesecna cijena (EUR):', monthly_price)
