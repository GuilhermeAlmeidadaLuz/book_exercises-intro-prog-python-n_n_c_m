# Data: 02/09/2024

# ============ EXERCÍCIO 3.10 ====================

# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem
# do aumento. Exiba o valor do aumento e do novo salário.

def increase_salary(earnings, percentage):
    increase =  earnings * percentage
    new_salary = earnings + increase
    return new_salary

if __name__=="__main__":
    print()
    print('========= Salary increment ===========\n')
    salary = float(input("Enter the salary: "))
    percentageToRaise = float(input("Enter the increase percentage: "))
    percentageToRaise /= 100
    print()
    print(f"New salary with increase is: {increase_salary(salary, percentageToRaise)}")
    print()