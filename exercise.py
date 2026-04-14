import os
nome_funcionario = input("Informe o seu nome: ")
print("1 - Gerente")
print("2 - Analista")
print("3 - Assistente")
print("4 - Estagiário")
cargo = int(input("Selecione o seu cargo: "))
salario_base = float(input("Informe o seu salário base: "))
total_horas_extras = float(input("Informe o total de horas extras trabalhadas no mês: "))
total_faltas_mes = int(input("Informe o total de faltas no mês: "))
bonus_recebido = input("Recebeu bônus de desempenho? (s/n): ").lower()
os.system("cls" if os.name == "nt" else "clear")
def calcular_horas_extras(salario_base,total_horas_extras):
    return (salario_base*0.015)*total_horas_extras

def calcular_desconto_faltas(salario_base,total_faltas_mes):
    return (salario_base*0.02)*total_faltas_mes

def calcular_bonus(cargo,bonus_recebido):
    bonus=0
    if bonus_recebido== "s":
        if cargo== 1:
            bonus= 1000
        elif cargo== 2:
            bonus= 500
        elif cargo== 3:
            bonus= 300
        elif cargo== 4:
            bonus= 100
    else:
        bonus= 0
    return bonus

total_acrescentado= calcular_horas_extras(salario_base,total_horas_extras) + calcular_bonus(cargo,bonus_recebido)
total_desconto= calcular_desconto_faltas(salario_base,total_faltas_mes)
valor_final=salario_base + total_acrescentado - total_desconto
print(f"""
-----------RESULTADOS-----------
Nome Usuario: {nome_funcionario}
Salario bruto: {salario_base:.2f}
Total de acrescimo(horas extras e bonus): {total_acrescentado:.2f}
Total de desconto(faltas): {total_desconto:.2f}
Salario final: R${valor_final:.2f}
--------------------------------
""")