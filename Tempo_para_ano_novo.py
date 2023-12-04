segundos_por_minuto = 60
segundos_por_hora = 60 * 60
segundos_por_dia = 24 * 60 * 60

import time

agora = time.localtime()
proximo_ano = (agora.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0)

diferenca = int(time.mktime(proximo_ano) - time.mktime(agora))

# Calcula o número de dias restantes
dias_restantes = diferenca // segundos_por_dia

# Calcula o número de horas restantes
horas_restantes = (diferenca - dias_restantes * segundos_por_dia) // segundos_por_hora

# Calcula o número de minutos restantes
minutos_restantes = (diferenca - dias_restantes * segundos_por_dia - horas_restantes * segundos_por_hora) // segundos_por_minuto

# Calcula o número de segundos restantes
segundos_restantes = diferenca - dias_restantes * segundos_por_dia - horas_restantes * segundos_por_hora - minutos_restantes * segundos_por_minuto

# Imprime a saída
print(f"Faltam {dias_restantes:.0f} dias, {horas_restantes:.0f} horas, {minutos_restantes:.0f} minutos e {segundos_restantes:.0f} segundos.")
