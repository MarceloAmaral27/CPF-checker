def calculo_cpf(counter, cpf):
    """ Efetua a soma dos digitos do cpf multiplicados pelo counter

    Args:
        counter: Contador
        cpf: cpf contendo nove ou dez digitos, que será multiplicado pelo antecessor do counter

    Returns:
        retorna a soma dos digitos multiplicados pelo counter
    """
    total_sum = 0
    for digit in cpf:
        total_sum += int(digit) * counter
        counter -= 1
    return total_sum


def texto(msg, tamanho):
    print('='*tamanho)
    print(f'{msg:^{tamanho}}')
    print('='*tamanho)


def cores(indice):
    cores = (
    '\033[m', # [0] Limpa
    '\033[1;31m', # [1] Vermelho
    '\033[1;32m', # [2] Verde
    )
    return cores[indice]
