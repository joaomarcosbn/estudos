#Calculando a idade
#Um usuário fornece sua data de nascimento no formato "dd/mm/aaaa".
#Crie um script Python que calcula a idade do usuário.

from datetime import datetime
import time
day = int(input('Insert the day of your born: '))
month = int(input('Insert the month of your born: '))
year = int(input('Insert the year of your born: '))

today_time = datetime.now()
born = datetime(year, month, day)

diference = today_time.year - born.year

today_month = today_time.month
today_day = today_time.day

born_month = born.month
born_day = born.day

if born_month > today_month:
    diference -= 1
elif born_month == today_month and born_day > today_day:
    diference -= 1


print(diference)