faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

# você precisa inserir no sistema um dicionário no formato:
#transformar o alor em numero
# calcular o imposto mensal
#calcular o imposto trimestral
def transformar_numero(valor):
    #Tirando o R$
    valor = valor.replace("R$ ", "")
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")
    valor = float(valor)
    return valor

def calcular_mensal(valor):
    iss = valor * 0.05
    pis = valor * 0.0065
    cofins = valor * 0.03
    mensal = iss + pis + cofins
    return mensal

def calcular_trimestral(valor):
    ir = valor * 0.048
    if valor > 20000:
        ir2 = (valor - 20000) * 0.1
    else:
        ir2 = 0
    pis = valor * 0.0065
    csll = valor * 0.0288 * valor
    trimestral = ir + ir2 + csll
    return trimestral

cont = 0
soma = 0
for mes in faturamento:
    valor = transformar_numero(faturamento[mes])
    cont += 1
    mensal = calcular_mensal(valor)
    soma = valor
    if cont == 3 or cont == 6 or cont == 9 or cont == 12:
        trimestral = calcular_trimestral(soma)
    else:
        trimestral = 0
    faturamento[mes] = (valor, mensal, trimestral)
print(faturamento)        
    