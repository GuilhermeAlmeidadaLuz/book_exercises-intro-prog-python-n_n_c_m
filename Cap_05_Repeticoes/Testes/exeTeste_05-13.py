# Data: 10/03/2025

# ============ EXERCÍCIO 5.13 (PÁG. 90) ============

''' Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o
valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total
de juros pago. '''

# valor_inicial_divida = float(input("Digite o valor inicial da sua dívida: R$ "))
# juros_mensal = float(input("Digite a taxa de juros mensal (0% ... _%): "))/100
# print(juros_mensal)

# pagamento_mensal = float(input("Qual valor a ser pago mensalmente: R$ "))

# num_meses_a_pagar = 0
# total_pago = 0

# passou = 0
# valor_atual_divida = valor_inicial_divida

# while valor_atual_divida > 0:
#     valor_atual_divida -= pagamento_mensal    # retira da dívida o pagamento mensal
#     num_meses_a_pagar += 1                      # acumulador para meses a pagar
#     if valor_atual_divida <= 0:
#         passou = passou - valor_atual_divida
#         ultima_parcela = pagamento_mensal - passou
#         pagamento_mensal = ultima_parcela
    
#     total_pago += pagamento_mensal              # acumula o total pago em todos os meses

#     valor_atual_divida += (valor_atual_divida * juros_mensal)

# total_pago_em_juros = total_pago - valor_inicial_divida

# print(f"Número de meses para que a dívida seja paga: {num_meses_a_pagar}", end= " mês(es)\n"
#       f"Total pago: R$ {total_pago:>8.2f}\n"
#       f"Total de juros pagos: R$ {total_pago_em_juros:>8.2f}")

# -----------------------------------------
# -------------------------------------------
# ---------------------------------------------
# ---------------------------------------------

# while valor_atual_divida > 0:
#     valor_atual_divida += (valor_atual_divida * juros_mensal)
    
#     valor_atual_divida -= pagamento_mensal    # retira da dívida o pagamento mensal
#     num_meses_a_pagar += 1                      # acumulador para meses a pagar
#     print(f"Dívida restante: {valor_atual_divida:>.2f} no mês {num_meses_a_pagar} de pagamento")
#     if valor_atual_divida < pagamento_mensal:
#         break
    
#     total_pago += pagamento_mensal              # acumula o total pago em todos os meses

    

# total_pago_em_juros = total_pago - valor_inicial_divida

# #############################
# print(f"\nNúmero de meses para que a dívida seja paga: {num_meses_a_pagar}", end= " mês(es)\n"
#       f"Total pago: R$ {total_pago:>8.2f}\n"
#       f"Total de juros pagos: R$ {total_pago_em_juros:>8.2f}")