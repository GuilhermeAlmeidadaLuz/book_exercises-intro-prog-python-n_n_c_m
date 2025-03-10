# Data: 10/03/2025

# ============ EXERCÍCIO 5.13 (PÁG. 90) ============

''' Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o
valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total
de juros pago. '''

valor_inicial_divida = float(input("Digite o valor inicial da sua dívida: R$ "))
juros_mensal = float(input("Digite a taxa de juros mensal (0% ... _%): "))/100

pagamento_mensal = float(input("Qual valor a ser pago mensalmente: R$ "))
print()

if valor_inicial_divida * juros_mensal >= pagamento_mensal:
    print("Impossível quitar a dívida, pois o valor a ser pago mensalmente é inferior ou igual ao juros mensal")

else:
    num_meses_a_pagar = 0
    total_pago = 0
    valor_atual_divida = valor_inicial_divida

    while valor_atual_divida > pagamento_mensal:
        valor_atual_divida = valor_atual_divida + (valor_atual_divida * juros_mensal)   # dívida acrescida dos juros, só amortizaria se pagasse à vista, como é parcelado, já é atualizada para valor com juros antes do 1º pagamento
        
        valor_atual_divida = valor_atual_divida - pagamento_mensal    # retira da dívida o pagamento mensal
        num_meses_a_pagar = num_meses_a_pagar + 1                      # acumulador para meses a pagar
        total_pago = total_pago + pagamento_mensal              # acumula o total pago em todos os meses sem incluir os juros
        print(f"Dívida restante: R$ {valor_atual_divida:>.2f} no {num_meses_a_pagar}º mês de pagamento")
    total_pago_em_juros = (total_pago + valor_atual_divida) - valor_inicial_divida

    print(f"\nNúmero de meses para que a dívida inicial seja paga: {num_meses_a_pagar}", end= " mês(es)\n"
            f"O juros mensal de {juros_mensal * 100:5.2f} % é aplicado sobre a dívida inicial de R$ {valor_inicial_divida:>8.2f}, o total pago ao final será: R$ {total_pago + valor_atual_divida:>8.2f}\n"
            f"Total de juros a ser pago: R$ {total_pago_em_juros:>8.2f}")