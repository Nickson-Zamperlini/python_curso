# Faça um programa que recebe o salário de um colaborador e o reajuste seguindo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_bruto = float(input("Digite seu sálario: "))
percentual = 0
valor_aumento = 0
salario_liquido = 0

if salario_bruto <= 280:
    percentual = "20%"
    valor_aumento = salario_bruto * 0.20
elif salario_bruto <= 700:
    percentual = "15%"
    valor_aumento = salario_bruto * 0.15
elif salario_bruto <= 1500:
    percentual = "10%"
    valor_aumento = salario_bruto * 0.10
else:
    percentual = "5%"
    valor_aumento = salario_bruto * 0.05

salario_liquido = salario_bruto + valor_aumento

print(f"Salario Bruto R${salario_bruto:.2f} \nPercentual {percentual} \nValor de Aumento R${valor_aumento:.2f} \nSalario Liquido R${salario_liquido:.2f}")