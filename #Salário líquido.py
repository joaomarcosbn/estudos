#Salário líquido
salario = int(input("Qual o seu salário por hora?"))
horas_trabalhadas = int(input("Quantas horas você trabalha por semana?"))
dias = str(input("Esse mês tem 31 dias? S/N"))
if (dias == "n"):
  mes = (horas_trabalhadas / 7) * 30
  total = salario * mes
  print(f'+ Salário bruto: R${total:,.2f}')
  ir = total * 0.11
  print(f'- Imposto de renda(11%): R${ir:,.2f}')
  inss = total * 0.08
  print(f'- INSS(8%): R${inss:,.2f}')
  sind = total * 0.05
  print(f'- Sindicato(5%): R${sind:,.2f}')
  liq = total - ir - inss - sind
  print(f'= Salário líquido: R${liq:,.2f}')
elif (dias == "s"):
  mes = (horas_trabalhadas / 7) * 31
  total = salario * mes
  print(f'+ Salário bruto: R${total:,.2f}')
  ir = total * 0.11
  print(f' Imposto de renda(11%): R$ {ir:,.2f}')
  inss = total * 0.08
  print(f'- INSS(8%): R${inss:,.2f}')
  sind = total * 0.05
  print(f'- Sindicato(5%): R${sind:,.2f}')
  liq = total - ir - inss - sind
  print(f'= Salário líquido: R${liq:,.2f}')