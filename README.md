# VALIDADOR DE CPF
Programa feito para verificar se um cpf é válido.

## Tecnologias usadas
- Linguagem Python

## Requisitos para o programa funcionar
- Possuir o python instalado em sua máquina

**Como Sabemos se um CPF é válido?**
Exemplo de cpf: 145.382.206-20

## PENULTIMO DIGITO

1- Começamos utilizando os 9 primeiros dígitos multiplicando-os pela sequência decrescente de 10 à 2;
    1 x 10
    4 x 9
    5 x 8
    ...

2 - Somamos todos os resultados das multiplicações;
    10 + 36 + 40 + 21 + 48 + 10 + 8 + 0 + 12 = 185

3 - Dividimos a soma por 11 e pegamos o módulo (resto) desta divisão;
    185 % 11 = 9

4 - Faça 11 - resto da divisão;

5 - Se o resultado for maior que 9, o penúltimo digito verificador será 0, caso o contrário será o resultado da subtração anterior

## uLTIMO DIGITO

1 - Utilizaremos os 10 primeiros digitos multiplicando-os pela sequência descrescente de 11 à 2;
2 - Repita todos os passos do penultimo digito a partir do segundo passo.