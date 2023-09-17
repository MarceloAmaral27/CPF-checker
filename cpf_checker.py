import sys
import re

cpf_sent_by_the_user = str(input('CPF que deseja verificar: ')).strip()
CPF_WITHOUT_POINTS = re.sub(r'[^0-9]', '', cpf_sent_by_the_user)
nine_digits_cpf = CPF_WITHOUT_POINTS[0:9]

checking_sequetial_input = CPF_WITHOUT_POINTS == CPF_WITHOUT_POINTS[0] * len(CPF_WITHOUT_POINTS)

if checking_sequetial_input:
    print('\033[1;31mVocê digitou números sequenciais\033[m!')
    sys.exit()

counter_1 = 10
total_sum = 0
for digit in nine_digits_cpf:
    total_sum += int(digit) * counter_1
    counter_1 -= 1

first_result_digit = (total_sum * 10) % 11
first_result_digit = first_result_digit if first_result_digit <= 9 else 0

ten_digits_cpf = nine_digits_cpf + str(first_result_digit)

counter_2 = 11
total_sum = 0
for digit in ten_digits_cpf:
    total_sum += int(digit) * counter_2
    counter_2 -= 1

second_result_digit = (total_sum * 10) % 11
second_result_digit = second_result_digit if second_result_digit <= 9 else 0

cpf_generated_with_calculation = nine_digits_cpf + str(first_result_digit) + str(second_result_digit)

if CPF_WITHOUT_POINTS == cpf_generated_with_calculation:
    print(f'O CPF {CPF_WITHOUT_POINTS} é válido.')
else:
    print(f'O CPF {CPF_WITHOUT_POINTS} não é válido.')

