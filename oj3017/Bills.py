"""Bills"""
price = float(input())
service_charge = price * 0.1
if service_charge <= 50:
    service_charge = 50
elif service_charge >= 1000:
    service_charge = 1000

Vat = (price + service_charge) * 0.07
total = price + service_charge + Vat

print(f"{total:.2f}")
