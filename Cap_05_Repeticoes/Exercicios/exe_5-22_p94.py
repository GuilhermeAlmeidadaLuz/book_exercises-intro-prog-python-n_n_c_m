# Data: 26/03/2025

# ============ EXERCÍCIO 5.22 (PÁG. 94) ============

# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e
# sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

# import os
while True:
      print(f'\n{'=' * 10} Menu {'=' * 10}\n'
          '1 - adição (+)\n'
          '2 - subtração (-)\n'
          '3 - multiplicação (x)\n'
          '4 - divisão (/)\n'
          '5 - sair\n'
          f'{'=' * 26}\n')
      opcao = int(input("Digite a opção: "))
      if opcao == 5:
            print("... Finalizando programa ...")
            break
      
      elif opcao >= 1 and opcao < 5:
            tabuada = int(input("Tabuada do número: "))
            numero = 1
            while numero <= 10:
                  if opcao == 1:
                        print(f'{tabuada:<2} + {numero:>2} = {tabuada + numero:>3}')
                  elif opcao == 2:
                        print(f'{tabuada:<2} - {numero:>2} = {tabuada - numero:>3}')
                  elif opcao == 3:
                        print(f'{tabuada:<2} x {numero:>2} = {tabuada * numero:>3}')
                  elif opcao == 4:
                        print(f'{tabuada:<2} / {numero:>2} = {tabuada / numero:>5.2f}')
                  numero += 1
            print(f'{'=' * 5} Fim da Tabuada {'=' * 5}\n')
      else:
            print('\nVocê não digitou uma opção válida, tente novamente!\n')     