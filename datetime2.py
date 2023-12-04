#Data e hora em diferentes fusos horários
#Uma empresa tem escritórios em São Paulo, Nova York e Tóquio.
#Crie um script Python que mostra a data e hora atuais nesses três fusos horários.
#Exiba, também, se estes escritórios estão abertos ou fechados (9h às 17h).

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

time_zone_sp = ZoneInfo("America/Sao_Paulo")
today_time = datetime.now()
time_zone_ny = ZoneInfo("America/New_York")
time_zone_tky = ZoneInfo("Asia/Tokyo")

datesp = today_time.astimezone(time_zone_sp)
date_sp = datesp.strftime("%d/%m/%m, %H:%M:%S") 
print("SP time: ", date_sp)

dateny = today_time.astimezone(time_zone_ny)
date_ny = dateny.strftime("%d/%m/%m, %H:%M:%S")
print("NY time: ", date_ny)

datetky = today_time.astimezone(time_zone_tky)
date_tky = datetky.strftime("%d/%m/%m, %H:%M:%S")
print("Tokyo time: ", date_tky)

def ver_hour(date_hour):
    if 9 <= date_hour.hour < 17:
        return "open"
    else:
        return "closed"

print(f'The Sao Paulo office is {ver_hour(datesp)}')
print(f'The New York office is {ver_hour(dateny)}')
print(f'The Tokyo office is {ver_hour(datetky)}')