import datetime

eclipse = datetime.date(2024, 4, 8) # 8 de abril de 2024
today = datetime.date.today()

delta = eclipse - today

if delta >= datetime.timedelta(0):
    print(f'Faltan {delta.days} días para el Eclipse Solar del 2024 en México.')
else:
    print(f'Han pasado {delta.days} días desde el Eclipse Solar del 2024 en México.')