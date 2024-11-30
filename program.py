# Função que multiplica os pesos
def calculo(pesos) -> int:
    lista_multiplicados: list = []  # Lista que vai guardar os resultados das multiplicações
    for digito in range(len(cpf)):
        if not cpf[digito].isdigit(): # Verificando se o digito é um número
            continue
        else:
            lista_multiplicados.append(int(cpf[digito]) * (pesos)) # Multiplicando o primeiro digito pelo peso
            pesos -= 1 
            # Caso faltem 2 digitos do cpf ele sai do loop
            if pesos < 2:
                break
    return 0 if 11 - (sum(lista_multiplicados) % 11) > 9 else 11 - (sum(lista_multiplicados) % 11)


# Inicio do programa
if __name__ == "__main__":
    cpf: str = input("CPF: ")

    # CALCULO PARA O PENULTIMO DIGITO
    penultimo_digito: int = calculo(10)

    # CALCULO PARA O ULTIMO DIGITO
    ultimo_digito: int = calculo(11)

    # Verificando se o CPF é válido
    if cpf[-2] + cpf[-1] == str(penultimo_digito) + str(ultimo_digito):
        print("\nCPF VÁLIDO")
    else: 
        print("\nCPF INVÁLIDO")