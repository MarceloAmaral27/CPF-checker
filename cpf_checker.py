import sys
import re
import modulo
from modulo import cores

modulo.texto('Verificador de CPF', 40)

cpf_sent_by_the_user = str(input('CPF que deseja verificar: ')).strip()
CPF_WITHOUT_POINTS = re.sub(r'[^0-9]', '', cpf_sent_by_the_user)
nine_digits_cpf = CPF_WITHOUT_POINTS[0:9]


checking_sequetial_input = CPF_WITHOUT_POINTS == CPF_WITHOUT_POINTS[0] * len(CPF_WITHOUT_POINTS)

if checking_sequetial_input:
    print(f'{cores(1)}Você digitou números sequenciais. Ex: 111.111.111-11{cores(0)}!')
    sys.exit()

# Está função retorna a soma dos números do cpf multiplicados por 10
calculation_result = modulo.calculo_cpf(10, nine_digits_cpf)

first_result_digit = (calculation_result * 10) % 11
first_result_digit = first_result_digit if first_result_digit <= 9 else 0

ten_digits_cpf = nine_digits_cpf + str(first_result_digit)

# Está função retorna a soma dos números do cpf multiplicados por 11
calculation_result = modulo.calculo_cpf(11, ten_digits_cpf)

second_result_digit = (calculation_result * 10) % 11
second_result_digit = second_result_digit if second_result_digit <= 9 else 0

cpf_generated_with_calculation = nine_digits_cpf + str(first_result_digit) + str(second_result_digit)

formatted_cpf = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', CPF_WITHOUT_POINTS)

# Verificando se o CPF enviado pelo usuário é válido
if CPF_WITHOUT_POINTS == cpf_generated_with_calculation:
    print(f'{cores(2)}O CPF {formatted_cpf} é válido.{cores(0)}')
else:
    print(f'{cores(1)}O CPF {formatted_cpf} não é válido.{cores(0)}')
