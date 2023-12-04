#Oferecendo desconto para cliente com base na última compra
#Crie um script Python que mostra quanto tempo se passou desde a última compra do cliente.
#Se faz mais de 30 dias, mostre uma mensagem oferecendo um desconto para o cliente.

from datetime import datetime, timedelta

today_date = datetime.now()

last_buy_date = datetime(2023, 10, 20)

date = today_date - last_buy_date

if date.days > 30:
    print("Congratulations, you have a discount")
else:
    print("You don't have any discount")